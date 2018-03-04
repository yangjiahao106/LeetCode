
-- 方法一： count 加条件
-- 判断方法一：round( count( if(T.status != 1,true,null)/count(*)), 2) Cancellation_Rate

select T.request_at Day,
      round( count( case when T.status != 1 then 1 else null end) / count(*), 2)
      as "Cancellation Rate"

from Trips T
inner join Users U on T.client_id = U.users_id
where U.Role = 'client' and u.banned = 'No' and
        T.request_at between '2013-10-01' and '2013-10-03'
group by T.request_at


-- 错误答案，查询不到取消率为零的情况。
select t1.request_at Day, round(count(T1.id) / al.all_status,2) Cancellation_Rate
from Trips T1
inner join Users U1 on T1.client_id = U1.users_id
inner join
            (select T2.request_at, count(*) all_status
            from Trips T2
            inner join Users U2 on T2.client_id  = U2.users_id
            where u2.Role = 'client' and u2.banned = 'No'
            group by T2.request_at ) al
            on al.request_at = T1.request_at

where u1.Role = 'client' and u1.banned = 'No'
        and T1.status in (2,3)
        and T1.request_at between '2013-10-01' and '2013-10-03'
group by t1.request_at
