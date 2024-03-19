#1. 입력받은 문자열과 숫자 분리
#2. 알파벳은 오름 차순 정리
#3. 숫자는 더해서 정리
#4. 이어붙이기

# 문자열 S
s= input()
save_alp=''
save_num=0
for letter in s:
    print(letter)
    if 65<=ord(letter) and ord(letter) <=90:
        save_alp=save_alp+letter
    else:
        save_num = save_num+int(letter)

save_alp=''.join(sorted(save_alp))
print(save_alp+str(save_num))
        
        
    
