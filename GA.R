
nd_msm_linha <- function(solucao)
{
  #teste
  #solucao = c(1,5,8,4,2,6,7,3)
  
  
  #inicializa um vetor com 196 posicoes preenchido com zeros
  vetor = rep.int(0,196)
  
  #variavel auxiliar
  posicao = 1
  
  #transforma a solucao em vetor com 210 posicoes
  for (i in 1:14) 
  {
    vetor[ posicao + solucao[i] -1       ] = 1;
    posicao = posicao + 14
  }
  
  #tranforma o vetor em uma matriz 14 x 14
  queens = matrix(vetor, nrow=14,ncol=14,byrow =F)
  
  #variavel para contar os ataques
  total = 0 
  
  #verifica linhas e colunas
  for (i in 1:14) 
  {
    #verifica colunas
    total = total + ifelse(sum(queens[,i])>1,1,0)
    #verifica linhas
    total = total + ifelse(sum(queens[i,])>1,1,0)
  }
  
  
  total=total-choose_navios(solucao)
  return(-total)
  
}

choose_navios<-function(solucao)
{
  vetor=c(5,4,4,2,2,2,-2,-3,-3,-3)
  total=0
  for(i in 1:14)
  {
    x=sample(1:10,1)
    soma=solucao[[i]]+vetor[x]
    if(i<14)
    {
      z=i+1
      for(j in z:14)
      {
        total=total+ifelse(soma==solucao[[j]],1,0)
      } 
    }
  }
  return (-total)
  
}

library(GA)


#algoritmo genetico
resultado <- ga(type="permutation", fitness=nd_msm_linha,lower=c(1,1,1,1,1,1,1,1,1,1,1,1,1,1), upper=c(14,14,14,14,14,14,14,14,14,14,14,14,14,14),popSize = 10, maxiter = 1000)

vet<-summary(resultado)$solution[1,]
vet
