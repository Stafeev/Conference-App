def fruits(file):
    for fruit in file:
        name=fruit["name"]
        num_baskets=0
        num_fruit=0
        for item in fruit["baskets"]:
            num_baskets+=1
            num_fruit+=item
        print name,num_baskets,num_fruit

file=[
{ "name" : "apples",
"baskets" : [10,20,30]
},
{ "name" : "bananas",
"baskets" : [5,20,10,10]
}
]
fruits(file)
