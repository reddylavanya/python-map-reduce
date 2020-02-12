s = open("02.txt","r")
r = open("03.txt", "w")

Key = ""
Count = 0.0

for line in s:
  data = line.strip().split('\t')
  paymentType, amount = data

  if paymentType != Key:
    if Key:
      # output the last key value pair result
      r.write(Key + '\t' + str(Count)+'\n')

    # start over when changing keys
    Key = paymentType 
    Count = 0.0
  
  # apply the aggregation function
  #thisValue += float(amount)
  Count += 1

# output the final entry when done
r.write(Key + '\t' + str(Count)+'\n')

s.close()
r.close()