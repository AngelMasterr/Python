def solve(s):
    #name = s.title()              
    palabras = s.split()
    patata = s.split(" ")    
  
    for i in range(len(patata)):
        if patata[i] == "":
            patata[i] = patata[i]
        elif not patata[i][0].isdigit():
            patata[i] = patata[i].title()
        
    resultado = ' '.join(patata)
    
    return resultado
print(solve("asdasd asdasda 142asd   a  asdas 14255asd"))