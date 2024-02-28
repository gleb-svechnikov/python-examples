a = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
b = ['ორშაბათი', 'სამშაბათი', 'ოთხშაბათი', 'ხუთშაბათი', 'პარასკევი', 'შაბათი', 'კვირა']
for i in range(len(a)):
    a[i] = b[i]
for j in range(len(a)):
    print(a[j])