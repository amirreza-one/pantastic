import math

def encode_message(raw_input):
  raw_input = raw_input.replace(' ','')
  L = len(raw_input) 
  col = math.ceil(math.sqrt(L))
  row = math.ceil(L/col)

  encoded_list = []
  i = 0
  for i in range(col):
    encoded_word = ''
    for j in range(row):
      m = i+col*j
      if m < L:
        encoded_word += raw_input[m]
    encoded_list.append(encoded_word)
  return ' '.join(encoded_list)


sample_inputs = ['lookadistraction' , 'bananaerror' , 'chillout']
for sample in sample_inputs:
  print(f"Input : {sample}")
  print(f"Output : {encode_message(sample)}")
  print('---------')
