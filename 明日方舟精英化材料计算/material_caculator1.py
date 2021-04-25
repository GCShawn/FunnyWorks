
third_matrial = ['D32钢','双极纳米片','聚合剂']
second_material = ['RMA70-24','五水研磨石','三水锰矿','白马醇','酮阵列','改量装置','糖聚块','聚酸酯块','提纯源岩','异铁块']
first_material = ['酮凝集组','全新装置','异铁组','聚酸酯组','糖组','固源岩组','RAM70-12','研磨石','扭转醇','轻锰矿']
based_material = ['酮凝集','装置','异铁','聚酸酯','糖','固源岩']
#gray_material = ['双酮','破损装置','异铁碎片','酯原料','糖','源岩']

class Material:
    material_name = ''
    sub_material_and_number = []
    cost = 0

    def __init__(self,name,sub_material,cost):
        self.material_name = name
        self.sub_material_and_number = sub_material
        self.cost = cost

    def show(self):
        print(self.material_name)
        print(self.sub_material_and_number)
        print(self.cost)

    def sort(self):
        temp1 = self.sub_material_and_number[:]
        temp2 = []
        for i in temp1:
            if (type(i) == str)&(i not in temp2):
                temp2.append(i)

        l = len(temp2)
        j =0
        while j<=l:
            count = 0
            while (temp2[j] in self.sub_material_and_number):

                index = self.sub_material_and_number.index(temp2[j])+1
                count = count + self.sub_material_and_number[index]
                del self.sub_material_and_number[index-1]

            temp2.insert(j+1,count)
            j+=2
            l = len(temp2)
            if j>=l:
                break
        self.sub_material_and_number = temp2[:]

def made_by(name,*sub_material_material_number,cost):
    New_material = []
    New_cost = 0

    i=0
    while i <= (len(sub_material_material_number)-2):
        times = sub_material_material_number[i+1]
        for j in range(times):
            New_cost = New_cost + sub_material_material_number[i].cost
            New_material.extend(sub_material_material_number[i].sub_material_and_number)
        i+=2

    New_cost +=cost
    return_material = Material(name,New_material,New_cost)

    return_material.sort()

    return return_material


def main():

    #based_meterial = [0'酮凝集',1'装置',2'异铁',3'聚酸酯',4'糖',5'固源岩',6'RAM70-12', 7'研磨石', 8'扭转醇', 9'轻锰矿']
    Ketone_agglutination = Material(based_material[0],['酮凝集',1],0)
    Device = Material(based_material[1],['装置',1],0)
    Iso_iron = Material(based_material[2],['异铁',1],0)
    Polyester = Material(based_material[3],['聚酸酯',1],0)
    Sugar = Material(based_material[4],["糖",1],0)
    Solid_source_stone = Material(based_material[5],["固源岩",1],0)
    RMA7012 = Material(first_material[6],['RMA70-12',1],0)
    Grinding_stone = Material(first_material[7], ['研磨石', 1], 0)
    Reverse_alcohol = Material(first_material[8], ['扭转醇', 1], 0)
    Light_manganese_ore = Material(first_material[9], ['轻锰矿', 1], 0)

    # first_meterial = [0'酮凝集组', 1'全新装置',2'异铁组', 3'聚酸酯组', 4'糖组', 5'固源岩组', ]
    Solid_source_rock_group = made_by('固源岩组',Solid_source_stone,5,cost = 200)
    Sugar_group = made_by('糖组',Sugar,4,cost = 200)
    Polyester_group = made_by('聚酸酯组',Polyester,4,cost = 200)
    Iso_iron_group = made_by('异铁组',Iso_iron,4,cost = 200)
    New_device = made_by('全新装置',Device,4,cost = 200)
    Ketone_agglutination_group = made_by('酮凝集组',Ketone_agglutination,4,cost = 200)

    #second_meterial = [0'RMA70-24',1'五水研磨石',2'三水锰矿',3'白马醇',4'酮阵列',5'改量装置',6'糖聚块',7'聚酸酯块',8'提纯源岩',9'异铁块']
    RMA7024 = made_by('RMA70-24',Ketone_agglutination_group,1,Solid_source_rock_group,2,RMA7012,1,cost=300)
    Five_water_grinding_stone = made_by('五水研磨石',Grinding_stone,1,Iso_iron_group,1,New_device,1,cost=300)
    Manganese_ore = made_by('三水锰矿',Light_manganese_ore,2,Polyester_group,1,Reverse_alcohol,1,cost=300)
    White_horse_alcohol = made_by('白马醇',Reverse_alcohol,1,Sugar_group,1,RMA7012,1,cost=300)
    Ketone_array = made_by('酮阵列',Ketone_agglutination_group,2,Sugar_group,1,Light_manganese_ore,1,cost=300)
    Improved_device = made_by('改量装置',New_device,1,Solid_source_rock_group,2,Grinding_stone,1,cost=300)
    Sugar_agglomerate = made_by('糖聚块',Sugar_group,2,Iso_iron_group,1,Light_manganese_ore,1,cost=300)
    Polyester_block = made_by('聚酸酯块',Polyester_group,2,Ketone_agglutination_group,1,Reverse_alcohol,1,cost=300)
    Purified_source_rock = made_by('提纯源岩',Solid_source_rock_group,4,cost=300)
    Different_iron_block  = made_by('异铁块',Iso_iron_group,2,New_device,1,Polyester_group,1,cost=300)

    #third_metrial = [0'D32钢',1'双极纳米片',2'聚合剂']
    D32Steel = made_by('D32钢',Manganese_ore,1,Five_water_grinding_stone,1,RMA7024,1,cost = 400)
    Bipolar_nanosheet = made_by('双极纳米片',Improved_device,1,White_horse_alcohol,2,cost=400)
    Polymerizer = made_by('聚合剂',Purified_source_rock,1,Different_iron_block,1,Ketone_array,1,cost=400)
    SilverAsh = made_by('银灰',D32Steel,4,White_horse_alcohol,6,cost=180000)

    D32Steel.show()
    Bipolar_nanosheet.show()
    Polymerizer.show()
    SilverAsh.show()


if __name__ == '__main__':
    main()