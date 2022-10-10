import $ from "jquery";
import { appWindow } from '@tauri-apps/api/window';

$('#titlebar-minimize').on('click', () => appWindow.minimize());
$('#titlebar-close').on('click', () => appWindow.close());

let alwaysOnTop = false;
$('#titlebar-pin').on('click', () => {
  alwaysOnTop = !alwaysOnTop;
  $('#titlebar-pin').toggleClass('active');
  appWindow.setAlwaysOnTop(alwaysOnTop);
});