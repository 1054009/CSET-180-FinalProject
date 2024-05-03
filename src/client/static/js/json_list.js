export function isJSON(string)
{
	try
	{
		JSON.parse(string)
		return string.includes("{") || string.includes("[")
	}
	catch
	{
		return false
	}
}

export function fixJSONList(list) // Because I'm bad at handling JSON
{
	const parsedList = JSON.parse(list)
	if (!(parsedList instanceof Array))
		return parsedList

	const newList = []

	for (const block of parsedList)
	{
		if (!isJSON(block))
			continue

		const parsedBlock = JSON.parse(block)

		// Not perfect, but good enough
		if (parsedBlock.constructor == Object)
		{
			for (const [key, value] of Object.entries(parsedBlock))
			{
				if (isJSON(value))
					parsedBlock[key] = fixJSONList(value)
			}
		}

		newList.push(parsedBlock)
	}

	return newList
}
