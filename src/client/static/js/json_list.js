export function fixJSONList(list) // Because I'm bad at handling JSON
{
	const parsedList = JSON.parse(list)
	const newList = []

	for (const block of parsedList)
	{
		const parsedBlock = JSON.parse(block)

		// TODO: Check how arrays handle this

		newList.push(parsedBlock)
	}

	return newList
}
