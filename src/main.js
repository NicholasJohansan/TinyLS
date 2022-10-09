import $ from "jquery";
import mainHtml from './html/main.html?raw';
import titlebarHtml from './html/titlebar.html?raw';
import modeToggleHtml from './html/modeToggle.html?raw';
import urlBoxHtml from './html/urlBox.html?raw';
import.meta.globEager('./styles/*.css'); // import all css files

$('#titlebar').html(titlebarHtml);
$('#app').html(mainHtml);
$('#mode-toggle').html(modeToggleHtml);
$('#url-box').html(urlBoxHtml);

import { bindTitlebarEvents } from './titlebar';
import { bindModeToggle } from './modeToggle';
import { bindUrlBox } from './urlBox';
bindTitlebarEvents();
bindModeToggle();
bindUrlBox();