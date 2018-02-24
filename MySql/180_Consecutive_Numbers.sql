
#方法一: 结连三个logs

select distinct l1.Num ConsecutiveNums
from Logs l1, Logs l2, Logs l3
where l1.Id = l2.Id - 1 and l2.Id = L3.id -1
and l1.Num = l2.Num and l2.Num = l3.Num;

#方法二: 使用变量

select distinct Num from
   (SELECT Num,
            case
                when @record = Num then @count := @count + 1
                when @record <> @record:=Num then @count := 1
            end as n

     from Logs ,(select @count := 0, @record := Num from Logs limit 1) r) v
    ) a
    where a.n >= 3