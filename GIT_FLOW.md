# Git Flow - Guide d'utilisation

## Structure des branches

### Branches principales
- **main** : Branche de production (code stable en production)
- **develop** : Branche de développement (intégration des nouvelles fonctionnalités)

### Branches de support

#### Feature branches (fonctionnalités)
- **Préfixe** : `feature/`
- **Créée depuis** : `develop`
- **Fusionnée dans** : `develop`
- **Exemple** : `feature/user-authentication`, `feature/product-listing`

```bash
# Créer une nouvelle feature
git checkout develop
git checkout -b feature/nom-de-la-feature

# Terminer une feature
git checkout develop
git merge feature/nom-de-la-feature
git branch -d feature/nom-de-la-feature
```

#### Release branches (préparation de version)
- **Préfixe** : `release/`
- **Créée depuis** : `develop`
- **Fusionnée dans** : `main` et `develop`
- **Exemple** : `release/1.0.0`, `release/2.1.0`

```bash
# Créer une release
git checkout develop
git checkout -b release/1.0.0

# Terminer une release
git checkout main
git merge release/1.0.0
git tag -a v1.0.0 -m "Version 1.0.0"
git checkout develop
git merge release/1.0.0
git branch -d release/1.0.0
```

#### Hotfix branches (corrections urgentes)
- **Préfixe** : `hotfix/`
- **Créée depuis** : `main`
- **Fusionnée dans** : `main` et `develop`
- **Exemple** : `hotfix/critical-bug`, `hotfix/security-patch`

```bash
# Créer un hotfix
git checkout main
git checkout -b hotfix/nom-du-fix

# Terminer un hotfix
git checkout main
git merge hotfix/nom-du-fix
git tag -a v1.0.1 -m "Hotfix 1.0.1"
git checkout develop
git merge hotfix/nom-du-fix
git branch -d hotfix/nom-du-fix
```

## Workflow quotidien

### Pour développer une nouvelle fonctionnalité

1. Assurez-vous d'être à jour :
```bash
git checkout develop
git pull origin develop
```

2. Créez votre branche feature :
```bash
git checkout -b feature/ma-nouvelle-feature
```

3. Développez et committez régulièrement :
```bash
git add .
git commit -m "feat: description de la fonctionnalité"
```

4. Une fois terminé, fusionnez dans develop :
```bash
git checkout develop
git merge feature/ma-nouvelle-feature
git push origin develop
git branch -d feature/ma-nouvelle-feature
```

### Pour préparer une release

1. Créez la branche release depuis develop :
```bash
git checkout develop
git checkout -b release/1.0.0
```

2. Effectuez les derniers ajustements (version, changelog, etc.)

3. Fusionnez dans main et develop :
```bash
git checkout main
git merge release/1.0.0
git tag -a v1.0.0 -m "Version 1.0.0"
git push origin main --tags

git checkout develop
git merge release/1.0.0
git push origin develop

git branch -d release/1.0.0
```

### Pour un hotfix urgent

1. Créez la branche hotfix depuis main :
```bash
git checkout main
git checkout -b hotfix/bug-critique
```

2. Corrigez le bug et testez

3. Fusionnez dans main et develop :
```bash
git checkout main
git merge hotfix/bug-critique
git tag -a v1.0.1 -m "Hotfix 1.0.1"
git push origin main --tags

git checkout develop
git merge hotfix/bug-critique
git push origin develop

git branch -d hotfix/bug-critique
```

## Conventions de commit

- **feat**: Nouvelle fonctionnalité
- **fix**: Correction de bug
- **docs**: Documentation
- **style**: Formatage, point-virgules manquants, etc.
- **refactor**: Refactoring du code
- **test**: Ajout de tests
- **chore**: Tâches de maintenance

Exemple : `feat: add user authentication system`

## État actuel du projet

- ✅ Branche **main** : Production
- ✅ Branche **develop** : Développement actif
- 📝 Prêt pour créer des branches feature, release et hotfix
