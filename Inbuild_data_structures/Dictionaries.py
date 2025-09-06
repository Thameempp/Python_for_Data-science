
monthname = {
    "Jan" :" January",
    "Feb" :" February ",
    "Mar" :" March ",
    "Apr" :" April"
 }
# print(monthname[input("Enter month in short : ")])
print(monthname.get("Jan", "Not a valid key"))
