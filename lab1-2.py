score = int(input("รับค่าคะแนน:"))

if score>=101:
    print("กรุณารับป้อนข้อมูล 0-100")
    print("...")
    
elif score>=80:
    print("เกรด A")
elif score>=70:
    print("เกรด B")
elif score>=60:
    print("เกรด C")
elif score>=50:
    print("เกรด D")
elif score>=0:
    print("เกรด F")
    
elif score<0:
    print("กรุณารับป้อนข้อมูล 0-100")
    print("FAIL")