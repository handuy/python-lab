Định nghĩa biến jenkins_list là một list
Đọc dữ liệu file nj3_raw_tagging_valid_vms_15082022, lấy 2 cột Name và FutureState, lưu vào jenkins_list
Đọc dữ liệu file nj3_raw_tagging_invalid_vms_15082022, lấy 2 cột Name và FutureState, lưu vào jenkins_list

Định nghĩa biến randeep_list
Đọc dữ liệu file NJ3_1508, lấy 2 cột Name và FutureState, lưu vào biến randeep_list

Định nghĩa 2 biến vm_same, vm_diff
So sánh 2 biến jenkins_list và randeep_list:
    Chạy vòng lặp qua randeep_list:
        Nếu randeep_list[i] xuất hiện trong jenkins_list:
            append vào vm_same
        else
            append vào vm_diff

Viết giá trị 2 biến vm_same, vm_diff lần lượt vào 2 file excel