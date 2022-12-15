# Git Flow - dans dev
« Code Review process »

**Note : toutes les opérations ont été effectuées sur l'ordinateur du propriétaire dans le répertoire source (dev), au terminal, avec diverses commandes qui exploitent le CLI gh.**  

## 1.0 Lister et identifier le Pull Request (pr)
### 1.1 Dans le répertoire dev, au terminal :  

(base) dominique@fmm-pc3-ubuntu:~/dev$
> gh pr list  
Showing 1 of 1 open pull request in stardom1957/dev  

> gh pr list --web  
Ceci provoque l'ouverture de la page du pr sur mon GitHub dans mon navigateur web par-défaut.  Il est bien sûr possible de passer directement par GitHub (voir 1.2)  

Sur GitHub dans la page du pr :  
CLIC sur Update primes_GN.py  
--> l'adresse complète du pr se trouve sur la ligne d'adresse du navigateur : https://github.com/stardom1957/dev/pull/2  
  --> ou l'identité du pr est **2**  
(  
ALTERNATIVE : sur GitHub voir no du pr sous le titre du pr, ici no. 2 : **#2 opened 21 days ago by GuyNicol**  
)

### 1.2 ALTERNATIVE : passer par GitHub directement pour visualiser le pr.
... TODO : illustrer cette procédure  

Le no du pr est donc 2  

## 2.0 Tirer le contenu du pr vers le répertoire source (dev) sur la machine du propriétaire et en examiner le contenu 
### 2.1 Tirer le pr vers le répetoire source (dev) :
> gh pr checkout https://github.com/stardom1957/dev/pull/2  
remote: Enumerating objects: 11, done.  
remote: Counting objects: 100% (11/11), done.  
remote: Compressing objects: 100% (6/6), done.  
remote: Total 8 (delta 5), reused 4 (delta 2), pack-reused 0  
Unpacking objects: 100% (8/8), 2.54 KiB | 56.00 KiB/s, done.  
From https://github.com/stardom1957/dev  
 \* [new ref]         refs/pull/2/head -> patch-1  
 Switched to branch 'patch-1'  

(  
ALTERNATIVE gh pr checkout patch-1  
ALTERNATIVE gh pr checkout 2  
)

Je me retrouve donc directement dans la branche patch-1.  
> git branch  
(base) dominique@fmm-pc3-ubuntu:~/dev$ git branch  
  main  
 \* patch-1  
 
 Ensuite, j'examine l'état du repo de (local) :  
 > git branch
(base) dominique@fmm-pc3-ubuntu:~/dev$ git branch
  main
* patch-1

### 2.2 Examiner l'état des pr de la branche 
> gh pr status  

Relevant pull requests in stardom1957/dev  

Current branch  
  #2  Update primes_GN.py [GuyNicol:patch-1]  

Created by you  
  You have no open pull requests  **\* Note**

Requesting a code review from you  
  You have no pull requests to review  
  
  **\* Note** : cette branche patch-1 **est** un pr qui provient de GuyNicol, donc en effet, il n'y a pas de pr créé par moi pour cette branche !  

### Examiner et tester les changements proposés
Puisque j'ai le code en ma possession, il m'est maintenant possible de tester le code dans la branche patch-1 dans mon propre environnement de développement. Par la suite, je peux aller dans mon github repo pour commenter et peut être demander des changements à l'initiateur du pr.  Dans ce cas, je choisi de retourner dans GitHub pour congratuler G pour son travail, approuver et fusionner (merge) le pr dans main et fermer le pr.  
