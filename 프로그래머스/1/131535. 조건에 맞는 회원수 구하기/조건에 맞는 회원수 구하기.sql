SELECT count(USER_ID) as USERS
FROM USER_INFO
WHERE YEAR(JOINED)=2021 and AGE>19 and AGE<30