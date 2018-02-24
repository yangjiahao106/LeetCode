select s.Score, t.Rank from (
    select @row_num:=@row_num+1 Rank, Score from (
         select Score from Scores group by Score desc
    ) t1 join (
        select @row_num := 0 from dual
    ) t2
) t, Scores s where s.Score=t.Score group by Score desc, Rank asc, Id;