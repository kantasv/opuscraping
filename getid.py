# coding: UTF-8

#処理速度はhtmlを始めに削れば改善できる
#全ての科目を集めてtxtファイルのしてから扱いやすく処理する
import requests
URL="http://www0.osakafu-u.ac.jp/syllabus/detail.aspx?CD=4653"
r = requests.get(URL)


#setting id
htidlist=[
"lbl_KAMOKU_NM",
#"lbl_KAMOKU_NM_E",
"lbl_ZYUGYO_CD",
"lbl_TANI",
"lbl_HAITO",
"lbl_GAKKI_NM",
"lbl_KAMOKU_BUNRUI",
#"lbl_NUMBER_CD",
"lbl_WJ_NM","lbl_ROOM_NM",
#"lbl_KYOIN_NM"
]

htidsync=[
"科目",
#"SUBJECT",
"授業コード","単位数",
"配当年次","学期","科目分類",
#"ナンバリングコード",
"曜日コマ","教室",
#"担当教員"
]

save=open('htmlop.txt','a')
save.write('****\n') 
for i in range(len(htidlist)):
    
    string=r.content
    
    htid=htidlist[i]
    
#eliminating strings before htid
    fs=string.find(htid)
    string=string[fs+2:]
    string=string[len(htid):]
#detectng and eliminating strings after </span>
    fe=string.find('</span>')
    string=string[:fe]
    mes=htidsync[i]+":"+str(string)
    print(mes)
    save.write(mes+'\n')

save.close()
