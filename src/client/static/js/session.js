import { Helper } from "./JSModules/helper.js"

const g_Helper = new Helper()

g_Helper.hookEvent(window, "load", false, () =>
{
	document.body.g_SessionData = SESSION // Make sure everyone can access it
	document.body.g_bSessionIsValid = g_Helper.getBoolean(g_SessionData)

	// TODO: Edit navbar
	console.log(SESSION)
})
