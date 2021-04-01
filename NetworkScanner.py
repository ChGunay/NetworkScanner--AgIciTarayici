import scapy.all as scapy

############################NetworkScanner Step-By-Step############################

#1)arp request
#2)brodcast
#3)responso

###################################################################################


arp_request_packet = scapy.ARP(pdst="192.168.1.1/16")#First, we create arp request packets for our target network.--Öncelikle hedef ağımız için arp istek paketleri oluşturuyoruz
#scapy.ls(scapy.ARP())
arp_brodcast_packet = scapy.Ether(dest = "ff:ff:ff:ff:ff:ff")#We create broadcast packages to make podcasts.--Podcast yapmak için yayın paketleri oluşturuyoruz.
#scapy.ls(scapy.Ether())
combined_packet = arp_brodcast_packet/arp_request_packet#Combining broadcast packages and request packets with the "/" sign to get a combined packet.--Birleşik bir paket elde etmek için yayın paketlerini ve istek paketlerini "/" işaretiyle birleştirmek.

(answered_list,unanswered_list) = scapy.srp(combined_packet,timout=1)#We save the responses from scapy.srp in tuple--Scapy.srp'den gelen yanıtları tuple olarak kaydediyoruz

answered_list.summary()#we summarize the result and print it out--sonucu özetliyoruz ve yazdırıyoruz
#result = scapy.srp(combined_packet,timeout=1)#We put the combined_backet we created into the scapy.srp function to broadcast. We also specify the broadcast response waiting time in timeout.--Oluşturduğumuz birleşik_backet'i yayınlanmak üzere scapy.srp işlevine koyduk. Zaman aşımındaki yayın yanıtı bekleme süresini de belirtiyoruz.
#print(result)