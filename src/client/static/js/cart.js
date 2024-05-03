import { Helper } from "./JSModules/helper.js"
import { DOMBuilder } from "./JSModules/dom_builder.js"

import { fixJSONList } from "./json_list.js"

const g_Helper = new Helper()
const g_Builder = new DOMBuilder()

var g_ItemList = []

g_Helper.hookEvent(window, "load", false, () =>
{
	g_ItemList = fixJSONList(CART_ITEMS)

	console.log(g_ItemList)
})
