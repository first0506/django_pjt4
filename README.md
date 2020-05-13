# Django_pjt4

## 구현과정 및 페어프로그래밍 느낀점

1. 먼저 모델링 작업을 페어와 협의했습니다.
   * User - name, email
   * Movie - title, poster_url
   * Review - movie(1:N), user(1:N), content, rank, like_users(M:N)
   * Comment - user(1:N), content, review(1:N), recommend(프로젝트 진행 중 이 필드는 사용하지 않기로 결정->좋아요로 대체)



2. accounts, review 앱 두개로 나눠 프로젝트를 진행했습니다. (저는 review를 맡았습니다.)



### 문제점

1. 관리자계정 생성과 마이그레이션 작업시 다음과 같은 에러가 발생했다.

   ```
   accounts.User.groups: (fields.E304) Reverse accessor for 'User.groups' clashes with reverse accessor for 'User.groups'.
           HINT: Add or change a related_name argument to the definition for 'User.groups' or 'User.groups'.
   ```

   -> `settings.py` 에 `AUTH_USER_MODEL = 'accounts.User'`를 적어주지 않아서 에러가 발생했다.



2. review생성시 movie를 선택하는 박스에서 movie의 제목이 아닌 객체 그대로 표시되어 어떤게 어느 영화인지 알아볼 수 없었다.

   -> `__str__` 함수를 이용해 사용자 편의성을 높였습니다.

   ```python
   class Movie(models.Model):
       title = models.CharField(max_length=100)
       poster_url = models.URLField(max_length=150)
   
       def __str__(self):
           return self.title
   ```

   

3. review의 좋아요 수를 표기할 때 숫자가 아예 뜨지 않았다.

   -> 오타조심!! (like_user -> like_users)

   ```html
   <p>좋아요 : {{ review.like_users.count }}</p>
   ```



- 저번 페어프로그래밍과 달리 앱 단위로 나누어 페어 프로그래밍을 진행했습니다. 그 때보다 MTV의 유연성이 높아진 것을 느꼈습니다. 같은 기능을 한 사람이 담당하다 보니 저번과 달리 변수 실수가 나오지 않았습니다. 또한 앱 별로 기능 구현을 마친 뒤 각자 앱 개발 중 안되는 부분을 서로서로 물어보며 실수를 고쳐나갈 수 있었습니다.