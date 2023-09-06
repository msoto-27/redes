pp :: (Integral a) => [[a]] -> [a]
pp [] = []
pp (x:xs) = [head x] ++ pp  xs