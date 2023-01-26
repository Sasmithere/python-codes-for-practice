#wap that accepts time period in seconds and converts it into "min:sec" form

x =float(input("Enter time period in Seconds :"))

print()

print("The given time in min:sec is = ", int((x)/60),"min",":",int(x - 60),"sec")
