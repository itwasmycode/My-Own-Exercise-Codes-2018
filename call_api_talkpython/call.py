import program

data = input("Enter the movie that you want to search from api")

datas = program.call_api(data)

print(f"There are {len(datas)} datas found ")
for idx, values in enumerate(datas):
    print(f"{idx+1} no data is {values.title}with {values.id} ")
