def get_value(exchange):
  if exchange[0] == "R" and exchange[1] == "R":
    return 0.0
  if exchange[0] == "R" and exchange[1] == "P":
    return -1.0
  if exchange[0] == "R" and exchange[1] == "S":
    return 1.0
  if exchange[0] == "P" and exchange[1] == "R":
    return 1.0
  if exchange[0] == "P" and exchange[1] == "P":
    return 0.0
  if exchange[0] == "P" and exchange[1] == "S":
    return -1.0
  if exchange[0] == "S" and exchange[1] == "R":
    return -1.0
  if exchange[0] == "S" and exchange[1] == "P":
    return 1.0
  if exchange[0] == "S" and exchange[1] == "S":
    return 0.0


