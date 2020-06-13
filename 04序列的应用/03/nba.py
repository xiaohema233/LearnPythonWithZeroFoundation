oldlist = ["迈克尔·乔丹", "卡里姆·阿布杜尔·贾巴尔", "哈基姆·奥拉朱旺", "查尔斯·巴克利", "姚明"]  # NBA名人堂原有人员
newlist = ["贾森·基德", "史蒂夫·纳什", "格兰特·希尔"]  # 新增人员列表
oldlist.extend(newlist)  # 追加新球星
print(oldlist)  # 显示新的NBA名人堂人员列表
