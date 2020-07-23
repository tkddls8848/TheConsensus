import matplotlib.pyplot as plt
from wordcloud import WordCloud

# 예시 텍스트
text = open('US_constitution', 'r', encoding='UTF-8').read()
# WordCloud 창 로드
wc = WordCloud(width=800, height=800, font_path='C:\WINDOWS\FONTS\MALGUNSL.TTF').generate(text)
# pyplot 창 구성 뒤 이미지 로드 후 실행
plt.figure(figsize=(12,12))
plt.imshow(wc)
plt.show()


