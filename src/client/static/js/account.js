import { Helper } from "./JSModules/helper.js"
import { DOMBuilder } from "./JSModules/dom_builder.js"

const g_Helper = new Helper()
const g_Builder = new DOMBuilder()

g_Helper.hookEvent(window, "load", false, () =>
{
	console.log(document.body.g_SessionData)
})
