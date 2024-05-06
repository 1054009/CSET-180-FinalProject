import { Helper } from "./JSModules/helper.js"
import { DOMBuilder } from "./JSModules/dom_builder.js"

import { fixJSONList } from "./json_list.js"

const g_Helper = new Helper()
const g_Builder = new DOMBuilder()

var g_OrderData = {}
var g_ItemList = []

g_Helper.hookEvent(window, "load", false, () =>
{
	g_OrderData = fixJSONList(ORDER_DATA)
	g_ItemList = fixJSONList(ORDER_ITEMS)
})
