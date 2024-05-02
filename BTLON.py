class Rule:
    def __init__(self, left, right): # hàm khởi tạo nhận vào vế trái, vế phải 
        self.left = left
        self.right = right

    def follows(self, facts): #kiểm tra xem trong các luật có vế trái thuộc giả thiết không
        for fact in self.left: 
            if fact not in facts:
                return False
        return True

    def __str__(self): #khi nhập a,b -> c left sẽ đc gán [a, b]  right = 'c' khi gọi phương thức này sẽ trả về chuỗi a ⋀ b -> c
        return " ⋀ ".join(self.left) + " -> " + self.right 
    
    
def locate(TGIAN, rules): #trả về SAT sau khi so sánh vế trái của rule với trung gian và thêm phần tử đó vào 
    SAT = set()
    for rule in rules:
        if all(left in TGIAN for left in rule.left): 
            SAT.add(rule) 
    return SAT


def suy_dien_tien(gia_thiet_ban_dau, rules, goal): #truyền vào giả thiết ban đầu, các luật, mục tiêu
    TGIAN = set(gia_thiet_ban_dau) #trung gian = giả thiết ban đầu 
    while True:
        SAT = locate(TGIAN, rules) 
        if not SAT:
            break
        r = SAT.pop() #lấy 1 rules từ tập sat để áp dụng  
        TGIAN.add(r.right) # thêm vế phải giả thiết vào trung gian 
        rules.remove(r) # bỏ rule vừa áp dụng ra khỏi danh sách sat
        if goal in TGIAN:
            return True # nếu mục tiêu trong tập trung gian => true 
    return False


def doc_luat(filename):
    rules = []
    with open(filename, 'r') as file: #mở file với chế độ chỉ đọc 
        for line in file: #với mỗi dòng trong file 
            parts = line.strip().split('->') #loại bỏ khoảng trắng đầu dòng, cuối dòng , tách thành 2 phần trái phải 
            if len(parts) != 2: #0 đúng đinh dạng bỏ qua 
                continue  # Bỏ qua dòng không đúng định dạng
            left = parts[0].strip().split(',') #chia chuỗi parts[0] thành một danh sách các chuỗi con bằng cách tách chúng ra bằng dấu phẩy (,), sau đó loại bỏ các khoảng trắng ở đầu
            right = parts[1].strip()
            rules.append(Rule(left, right)) #tạo mới đối tượng rule trong danh sách rules 
    return rules #trả về danh sách các đối tượng rule đọc từ văn bản 


def doc_gia_thiet(filename):
    with open(filename, 'r') as file: #mở dạng chỉ đọc 
        return file.readline().strip().split(',') #trả về 1 danh sách các giả thiết, loại bỏ đầu cuối (chia chuỗi ra bởi dấu ,)


def main():
    gia_thiet_ban_dau_file = input("Nhập tên tệp chứa giả thiết ban đầu: ")

    rules_file = input("Nhập tên tệp chứa luật: ")

    goal = input("Nhập mục tiêu cần chứng minh hoặc bác bỏ: ").strip()

    # Đọc dữ liệu từ các tệp
    gia_thiet_ban_dau = doc_gia_thiet(gia_thiet_ban_dau_file)
    rules = doc_luat(rules_file)

    # Thực hiện thuật toán suy diễn tiến và gán vào  biến result 
    result = suy_dien_tien(gia_thiet_ban_dau, rules, goal)

    # In kết quả
    if result:
        print("Mục tiêu '{}' có thể được chứng minh từ các giả thiết ban đầu.".format(goal))
    else:
        print("Mục tiêu '{}' không thể được chứng minh từ các giả thiết ban đầu.".format(goal))


if __name__ == "__main__":
    main()

#<---------------Thử chương trình với ví dụ 2 trong slide với 2 file gia_thiet.txt và tep_chua_luat.txt---------------->

