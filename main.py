print(" MAIN FILE STARTED")

from graph import app

print(" GRAPH IMPORTED SUCCESSFULLY")

result = app.invoke({})

print(" GRAPH EXECUTION FINISHED")

print("\n FINAL OUTPUT:\n")
print(result)