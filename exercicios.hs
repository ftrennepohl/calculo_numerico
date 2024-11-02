-- 1.
salLiquido :: Float -> Float
salLiquido x = x + x * 0.1 - x * 0.07

-- 2.
notafinal :: Float -> Float -> Float -> Char
notafinal x y z | media > 8 = 'A'
                | media > 7 = 'B'
                | media > 6 = 'C'
                | media > 5 = 'D'
                | otherwise = 'E'
    where media = (x * 2 + y * 3 + z * 5) / 10

-- 3.
precoRetrato :: Integer -> String -> Double
precoRetrato qtd dia | qtd > 7 = f 185.0 dia 
                     | qtd == 6 = f 180.0 dia
                     | qtd == 5 = f 175.0 dia 
                     | qtd == 4 = f 165.0 dia
                     | qtd == 3 = f 150.0 dia
                     | qtd == 2 = f 130.0 dia
                     | qtd == 1 = f 100.0 dia  
    where
        f val dia = if dia == "domingo" || dia == "sábado" then val + val * 0.2 else val

-- 4.
fatDuplo x = if x == 0 || x == 1
                then 1
                else fatDuplo (x-2) * x

--5.
pot x n | n == 0 = 1
        | n == 1 = x
        | otherwise = x * pot x (n-1)

--6.
aumentoSal sal ac aa | aa == ac = sal
                     | aa - ac == 1 = sal * 0.015 + aumentoSal sal ac (aa-1)
                     | otherwise = 0.015 * (2 * (aa-ac-1)) * sal_anterior + sal_anterior where
                        sal_anterior = aumentoSal sal ac (aa-1)

--7.
ultimo (x:xs) = if null xs then x else ultimo xs

--8.
primeiros (x:xs) = if null xs then [] else x : primeiros xs

--9.
produtoListas lst1 lst2 = if null (tail lst2) || null (tail lst2) then head lst1 * head lst2 : [] else head lst1 * head lst2 : produtoListas (tail lst1) (tail lst2)

--10.


data Produto = Perecivel Integer String Int Char Forma
            | NaoPerecivel Integer String String Int Forma

codProduto :: Produto -> Integer
codProduto produto = case produto of
                        Perecivel cod _ _ _ _    -> cod
                        NaoPerecivel cod _ _ _ _  -> cod

--11.

data Forma = Unidade | Peso
                deriving Show

formaComercializacaoProduto :: Produto -> Forma
formaComercializacaoProduto produto = case produto of
                        Perecivel _ _ _ _ f    -> f
                        NaoPerecivel _ _ _ _ f  -> f

--12.
produtoValido :: Produto -> Int -> Bool
produtoValido produto aa = case produto of
                        Perecivel _ _ ano _ _   -> if ano > aa then False else True 
                        NaoPerecivel _ _ _ _ _  -> True

--13.
and :: Bool -> Bool -> Bool
and