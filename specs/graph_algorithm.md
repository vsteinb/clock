```python
def straightBranches(layer, layerIndex = 0, activeBranches = []):

	# no commits left
	if not len(layer):
		return []

	# initial layer
	if layerIndex == 0:
		activeBranches = layer

	# all others
	else:

		for commit in layer:

			# got no parent!?
			if not len(commit.parents):
				throw "What the fuck?"

			# if commit is the first child of a parent, continue that column
			foundPlace = false
			for parent in commit.parents:
				if parent.children[0] == commit:

					# replace parent by commit in branches
					index = activeBranches.index(parent)
					activeBranches[index] = commit
					commit.j = index
					foundPlace = true
					break
			if foundPlace: continue

			# TODO check if a merge commit destroys the order. e.g. if it is the first child of two parents at the same time.
			# that would eventually result in commits of those branches to be blocked


			# compute free j-coordinates
			freeColumns = [index for index, value in enumerate(B) if value == None]

			if len(freeColumns):

					# occupy free column by commit in activeBranches
					# !TODO make the choosing more intelligent
					activeBranches[ activeBranches.index(freeColumns[0]) ] = commit
			else:
				# insert commit
				activeBranches.append(commit)

		# purge all ended branches of activeBranches
		for index in range(len(activeBranches)):
			if activeBranches[index] not in layer: activeBranches[index] = None

	return [activeBranches] + straightBranches([...c.children for c in layer], layerIndex + 1, activeBranches)
```
