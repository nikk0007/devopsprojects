create kind cluster:
- k create cluster --name cluster1
- kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.13.11/config/manifests/metallb-native.yaml
- k apply -f ip-pool.yaml
- kubectl get IPAddressPool -n metallb-system
- k apply -f L2Advertisement.yaml
- k get L2Advertisement -n metallb-system

TBD:
find the correct IP address range to be allocated to ip-pool. This can be checked by logging in to our router and check DHCP settings. This is where you'll find information about your local network's IP address range. In the DHCP settings, you'll typically find the "Start IP Address" and "End IP Address" or a "Subnet Mask" setting. MetalLB will need a range of IP addresses from within your local network's IP address range. You can choose a subset of IP addresses that are not used by DHCP to avoid conflicts. For example, if your local network's IP range is 192.168.0.100 to 192.168.0.200, you can allocate a range like 192.168.0.201 to 192.168.0.220 for MetalLB.