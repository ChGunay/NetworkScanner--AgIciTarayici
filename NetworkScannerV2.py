import scapy.all as scapy
import optparse

############################NetworkScanner Step-By-Step############################

#1)arp request
#2)brodcast
#3)responso

###################################################################################
def get_user_input():#We created the function to get input from the user--Kullanıcıdan girdi almak için işlevi oluşturduk
    opt_object = optparse.OptionParser()##We create an object using the optparse library and using this object we can get options from the user.--Optparse kütüphanesini kullanarak bir nesne oluşturuyoruz ve bu nesneyi kullanarak kullanıcıdan seçenekler alabiliyoruz.
    opt_object.add_options("-r","range",dest = "range", help="enter to range")#We direct the options we receive from the user to the variables in the script with dest.--Kullanıcıdan aldığımız seçenekleri dest ile betikteki değişkenlere yönlendiriyoruz.
    (user_input,arguments) = opt_object.parse_args() 
    if not user_input.range:
        print("Enter range address")
        
    return user_input
        

def scan_my_network(r):
    arp_request_packet = scapy.ARP(pdst=r)#First, we create arp request packets for our target network.--Öncelikle hedef ağımız için arp istek paketleri oluşturuyoruz
    #scapy.ls(scapy.ARP())
    arp_brodcast_packet = scapy.Ether(dest = "ff:ff:ff:ff:ff:ff")#We create broadcast packages to make podcasts.--Podcast yapmak için yayın paketleri oluşturuyoruz.
    #scapy.ls(scapy.Ether())
    combined_packet = arp_brodcast_packet/arp_request_packet#Combining broadcast packages and request packets with the "/" sign to get a combined packet.--Birleşik bir paket elde etmek için yayın paketlerini ve istek paketlerini "/" işaretiyle birleştirmek.
    
    (answered_list,unanswered_list) = scapy.srp(combined_packet,timout=1)#We save the responses from scapy.srp in tuple--Scapy.srp'den gelen yanıtları tuple olarak kaydediyoruz
    answered_list.summary()#we summarize the result and print it out--sonucu özetliyoruz ve yazdırıyoruz

userinput= get_user_input()
scan_my_network(userinput.range)
#result = scapy.srp(combined_packet,timeout=1)#We put the combined_backet we created into the scapy.srp function to broadcast. We also specify the broadcast response waiting time in timeout.--Oluşturduğumuz birleşik_backet'i yayınlanmak üzere scapy.srp işlevine koyduk. Zaman aşımındaki yayın yanıtı bekleme süresini de belirtiyoruz.
#print(result)