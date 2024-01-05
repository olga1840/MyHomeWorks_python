time = int(input('Введите  количество секунд: '))
result_hour = int(time//3600)
result_min = int((time%3600)//60)
result_sec = int((time%3600)%60)
print(f'В указанном количестве секунд {time}:\nчасов:{ result_hour}\nминут:{ result_min}\nсекунд:{ result_sec}')


temp = int(input('Введите температуру в градусах Цельсия: '))
result_K = float(temp*274.15)
result_F = float(temp*33.8)
result_R = float(temp*0.8)
print(f'В указанном количестве градусов Цельсия {temp}:\nградусов Кельвина:{ round(result_K,2)}\nградусов Фаренгейта:{ round(result_F,2)}\nградусов Реомюра:{ round(result_R,2)}')
