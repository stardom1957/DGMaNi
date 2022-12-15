# À la découverte de Git Flow
## Un exemples dans dev
« Code Review process » de la part du propriétaire du repo GitHub.

Notes :  
* Certaines des opérations de revue du pr mentionné plus bas ont été effectuées sur l'ordinateur du propriétaire dans le répertoire source (dev), au terminal, avec diverses commandes qui exploitent le CLI gh, alors que d'autres ont été exécutées sur GitHub, toujours dans le repo du propriétaire. Il s'agit bien sûr d'une manière de faire et nous sommes conscient qu'il y en a bien d'autres.  
* Pour garder les choses simples, le propriétaire ne s'est pas engagé dans le processus de commentaires et demandes de changements au code proposé dans ce pr, donc toutes les opérations illustrées plus bas ont été effectuées par le propriétaire du repo dev sans aucune intervention de la part de l'initiateur du pr (G).  
* Ainsi, dans cet exercice, le rôle de G a été d'initier le pr en passant par un « fork » du repo, avec création automatique de la branche **patch-1**. Dans cet pr, c'est cette branche qui est examinée plus bas.  

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
Unpacking object`s: 100% (8/8), 2.54 KiB | 56.00 KiB/s, done.  
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

## 3.0 Examiner et tester les changements proposés
Il m'est maintenant possible de tester le code dans la branche patch-1 dans mon propre environnement de développement. Par la suite, je pourrais aller dans mon remote repo pour commenter et peut être demander des changements à l'initiateur du pr. Cependant, puisque je suis déjà très satisfait des changements proposés, je choisi de retourner dans mon remote repo pour congratuler G pour son travail, approuver et fusionner (merge) le pr dans main et fermer le pr.  

### 3.1 Dans le remote repo, approuver, fusionner et fermer le pr
... TODO : à documenter  

## 4.0 Tirer les changements du remote repo vers le repo local  
> git checkout main  
Switched to branch 'main'  

> git pull origin main  
From https://github.com/stardom1957/dev  
 \* branch            main       -> FETCH_HEAD  
Updating 6f9d2dd..05138a7  
Fast-forward  
 python/primes_GN.py | 62 ++++++++++++++++++++++++++++++++++++++++++-----------  
 1 file changed, 50 insertions(+), 12 deletions(-)  

## En conclusion
On voit qu'il y a des étapes qui s'effectuent en ligne et d'autres qui se tiennent localement. Pour cet exercice, avec ce que je savais, j'ai choisi la voie qui me semblait la plus simple :
- utliser le CLI gh pour importer (tirer) le pr de mon remote repo vers mon local repo, avec le bénéfice de la création automatique de la branche patch-1  - ne pas m'engager dans le processus de commentaires et demandes de changements et de plutôt  
- approuver les changements, fusionner (merge) et fermer le pr sur le remote repo en une seule étape  

Puisque les changements ont été fusionnés en ligne, il devenait nécessaire à l'étape 4, de tirer (pull) ces changements de mon remote repo vers mon local repo.  
