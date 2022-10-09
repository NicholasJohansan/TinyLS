import $ from "jquery";
import mainHtml from './html/main.html?raw';
import titlebarHtml from './html/titlebar.html?raw';
import.meta.globEager('./styles/*.css'); // import all css files

$('#titlebar').html(titlebarHtml);
$('#app').html(mainHtml);

import { bindTitlebarEvents } from './titlebar';
bindTitlebarEvents();