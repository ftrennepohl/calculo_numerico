criterio_parada :: Double -> Double -> Double -> Bool
criterio_parada xn1 xn epsilon      | dif < epsilon = True
                                    | otherwise = False
                                    where dif = abs (xn1 -xn)

metodo_bisseccao :: (Double -> Double) -> Double -> Double -> Int -> Double -> (Double, Double)
metodo_bisseccao fun a b n epsilon | (b-a)/(2^n) < epsilon = (a, b)
                                   | fun x1 == 0 = (x1, x1)
                                   | fun a == 0 = (a, a)
                                   | fun b == 0 = (b, b)
                                   | otherwise = metodo_bisseccao fun a1 b1 (n+1) epsilon
                                    where a1 = if (fun x1 * fun a) > 0 then x1 else a
                                          b1 = if (fun x1 * fun b) > 0 then x1 else b
                                          x1 = (b+a)/2


metodo_posicao_falsa :: (Double -> Double) -> Double -> Double -> Int -> Double -> (Double, Double)
metodo_posicao_falsa fun a b n epsilon | (b-a)/(2^n) < epsilon = (a, b)
                                       | fun x1 == 0 = (x1, x1)
                                       | fun a == 0 = (a, a)
                                       | fun b == 0 = (b, b)
                                       | otherwise = metodo_posicao_falsa fun a1 b1 (n+1) epsilon
                                       where a1 = if (fun x1 * fun a) > 0 then x1 else a
                                             b1 = if (fun x1 * fun b) > 0 then x1 else b
                                             x1 = (a * fun b - b * fun a) / (fun b - fun a)

metodo_das_cordas :: (a -> a) -> (a -> a) -> a -> a -> a -> (Double, Double)
metodo_das_cordas fun fun_dx a b epsilon = 
      if fun a * fun_dx a > 0 then metodo_das_cordas_interno fun b a 2.2 0 epsilon else metodo_das_cordas_interno fun a b 2.2 0 epsilon

{-
b = extremo do intervalo fixo
c = extremo a ser calculado
xn = chute inicial
-}
metodo_das_cordas_interno :: (Double -> Double) -> Double -> Double -> Double -> Int -> Double -> (Double, Double)
metodo_das_cordas_interno fun b c xn n epsilon  | abs (xn1 - xn) < epsilon = (b, xn1)
                                                | fun (xn1) == 0 = (xn1, xn1)
                                                | fun c == 0 = (c, c)
                                                | otherwise = metodo_das_cordas_interno fun b c xn1 (n+1) epsilon
                                                where xn1 = xn - (fun (xn) / (fun (xn) - fun (c))) * (xn - c)