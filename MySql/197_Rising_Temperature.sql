
-- 方法一：
select w.Id
from Weather w
where w.temperature > (select temperature
                        from weather w2
                        where w2.date = date_add(w.date,interval -1 day))

-- 方法二：
select w1.Id
from Weather w1,Weather w2
where w1.temperature > w2.temperature
    and w1.date =  date_add(w2.date,interval 1 day)