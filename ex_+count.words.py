# x = 24
#
# if x < 0:
#     print(f'afara este inghetat')
# elif 0 <= x <= 15:
#     print(f'afara este frig')
# elif 15 <= x <= 30:
#     print(f'afara este placut')
# else:
#     print(f'afara este canicula')
#
# print('\n')
#
# referat = '''Python               is an interpreted high-levePython is an interpreted high-level general-purpose programming language. Its design philosophy emphasizes code readability with its use of significant indentation. Its language constructs as w
# ell as its object-oriented approach aim  to help       programmers write clear, logical code for smalll general-purpose programming language. Its design philosophy emphasizes code readability with its use of significant indentation. Its language constructs as well as
#  its object-oriented a     pproach aim to help      programmers write      clear, logical code for small
#  '''
#
# ref_count = referat.count('')
# if  ref_count <= 800:
#     print(f'{ref_count} insuficient')
# elif ref_count <= 1000:
#     print(f'{ref_count} suficient')
# else:
#     print(f'{ref_count}, prea mult')
#
# print('\n')

referat = '''Python is an interpreted high-levePython is an interpreted high-level general-purpose programming language. Its design philosophy emphasizes code readability with its use of significant indentation. Its language constructs as w
ell as its object-oriented approach aim  to h  elp       programmers write clear, logical code for smalll general-purpose programming language. Its design philosophy emphasizes code readability with its use of significant indentation. Its language constructs as well as
 its object-oriented a   pproach aim to      help      programmers write      clear, logical code for small
 '''

ref_split = referat.split(' ')
ref_caract = (len(referat))
ref_spa = len(ref_split)

dif = ref_caract - ref_spa

print(dif)

