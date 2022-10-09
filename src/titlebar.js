import $ from "jquery";
import { appWindow } from '@tauri-apps/api/window';

export const bindTitlebarEvents = () => {
  $('#titlebar-minimize').on('click', () => appWindow.minimize());
  // $('#titlebar-maximize').on('click', () => appWindow.toggleMaximize());
  $('#titlebar-close').on('click', () => appWindow.close());
};