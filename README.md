# django_instagram

python manage.py runserver 로 서버 실행 후 메인 홈페이지 이동 -> 로그인
![image](https://user-images.githubusercontent.com/99489461/208595884-990c5ce7-3a63-41f6-a552-6a163d4053a9.png)

로그인 성공 시 메인페이지로 이동합니다.
![image](https://user-images.githubusercontent.com/99489461/208596099-64c1d035-de43-4175-aa30-3ceaaa72307b.png)

좌측상단 로고와 우측 상단 홈 버튼을 클릭하면 메인페이지로 이동이 가능합니다.
우측 상단 프로필을 클릭하여 프로필 페이지 또는 로그아웃이 가능합니다.
![image](https://user-images.githubusercontent.com/99489461/208596240-0b146b61-187c-4377-9b4f-3c42310444ea.png)

-------------------------------------------------------------------------------------------------------------------------------

로그인 폼에서 회원가입을 클릭하여 회원가입 페이지로 이동 후 가입이 가능합니다.
![image](https://user-images.githubusercontent.com/99489461/208596529-6c797b50-9f62-4d0f-8116-7ede001629d3.png)

db sqlite3에서 가입한 회원 정보가 등록되었음을 확인 가능(user)
![image](https://user-images.githubusercontent.com/99489461/208596701-dd15b90b-8519-49ec-883b-5d87e686c78a.png)

-------------------------------------------------------------------------------------------------------------------------------

댓글창에 댓글 입력 후 게시를 클릭하면 댓글이 등록됩니다.
![image](https://user-images.githubusercontent.com/99489461/208596884-af80070e-0abf-4a34-95f4-8dd004e8f9e2.png)

sqlite3 에서 댓글이 등록되었음을 확인 가능(content_reply)
![image](https://user-images.githubusercontent.com/99489461/208597054-b09bc1ae-0e28-467f-af35-4d5ca32fcc21.png)

-------------------------------------------------------------------------------------------------------------------------------

좋아요(like)와 북마크 버튼을 클릭하면 아이콘이 바뀌며 좋아요와 북마크가 반영됩니다.
sqlite3 의 content_feed 와 content_like 에서 확인 가능합니다.
![image](https://user-images.githubusercontent.com/99489461/208597307-b79db379-5847-49d4-ae5c-c788eae776f0.png)

-------------------------------------------------------------------------------------------------------------------------------

우측 상단의 프로필을 눌러 마이페이지(마이프로필)로 이동이 가능
![image](https://user-images.githubusercontent.com/99489461/208597700-f65a8bba-6ea0-46b8-b733-8278405a3c0e.png)

게시글은 sqlite3 의 content_feed에서 확인이 가능합니다.
![image](https://user-images.githubusercontent.com/99489461/208597829-3d6dc79a-4d1a-4655-b29c-459b4bdc83cf.png)

마이프로필에서 자신이 좋아요와 북마크를 누른 게시물들을 확인할 수 있습니다.
![image](https://user-images.githubusercontent.com/99489461/208598030-2760c05a-8a2b-422b-a617-5e669b8d15b2.png)
![image](https://user-images.githubusercontent.com/99489461/208598066-8285b955-29d7-46bc-af3e-c4b942510764.png)

-------------------------------------------------------------------------------------------------------------------------------

프로필사진 편집을 클릭하여 원하는 사진으로 프로필 사진을 변경할 수 있습니다.
![image](https://user-images.githubusercontent.com/99489461/208598297-af786ae4-b314-4a4e-8237-9cdda32c97fb.png)
![image](https://user-images.githubusercontent.com/99489461/208598322-4ef6111a-fca8-421e-8dd7-7025818a1ef2.png)

-------------------------------------------------------------------------------------------------------------------------------

우측 상단 + 버튼을 클릭하여 게시물을 업로드 할 수 있습니다.
![image](https://user-images.githubusercontent.com/99489461/208598451-33039dc2-b032-48a4-98b2-4d5c2e54fc88.png)

이미지 파일을 드래그하여 올려놓으면 이미지가 등록되며 게시글 내용을 기재하여 공유 가능합니다.
![image](https://user-images.githubusercontent.com/99489461/208598637-46a5dcac-261b-42eb-acb3-8f827e2be693.png)
![image](https://user-images.githubusercontent.com/99489461/208598778-95f33544-dd6e-457a-b9b8-1c9b2d25850d.png)




