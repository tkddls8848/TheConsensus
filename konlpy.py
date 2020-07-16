from konlpy.tag import kkma

#자연어 해석 모듈 로드
kkma = kkma()
#문장을 형태소로 분해
print(kkma.sentence("안녕하세요. 제 이름은 박상인입니다."))
#문장의 명사만 추출
print(kkma.nouns("명사 형용사 부사 관계사 접속사 대명사"))
