import { createSvgIcon, SvgIconProps } from "@material-ui/core";
import React from "react";

const MiscellaneousIcon = createSvgIcon(
  <>
    <path
      fillRule="evenodd"
      clipRule="evenodd"
      d="M4.00037 2.375C3.1029 2.375 2.37537 3.10254 2.37537 4L2.37537 9C2.37537 9.89746 3.1029 10.625 4.00037 10.625H9.00037C9.89783 10.625 10.6254 9.89746 10.6254 9V4C10.6254 3.10254 9.89783 2.375 9.00037 2.375L4.00037 2.375ZM3.62537 4C3.62537 3.79289 3.79326 3.625 4.00037 3.625L9.00037 3.625C9.20747 3.625 9.37537 3.79289 9.37537 4V9C9.37537 9.20711 9.20747 9.375 9.00037 9.375H4.00037C3.79326 9.375 3.62537 9.20711 3.62537 9L3.62537 4Z"
      fill="currentColor"
    />
    <path
      fillRule="evenodd"
      clipRule="evenodd"
      d="M15.0004 2.375C14.1029 2.375 13.3754 3.10254 13.3754 4V9C13.3754 9.89746 14.1029 10.625 15.0004 10.625H20.0004C20.8978 10.625 21.6254 9.89746 21.6254 9L21.6254 4C21.6254 3.10254 20.8978 2.375 20.0004 2.375L15.0004 2.375ZM14.6254 4C14.6254 3.79289 14.7933 3.625 15.0004 3.625L20.0004 3.625C20.2075 3.625 20.3754 3.79289 20.3754 4L20.3754 9C20.3754 9.20711 20.2075 9.375 20.0004 9.375H15.0004C14.7933 9.375 14.6254 9.20711 14.6254 9V4Z"
      fill="currentColor"
    />
    <path
      fillRule="evenodd"
      clipRule="evenodd"
      d="M2.37537 15C2.37537 14.1025 3.1029 13.375 4.00037 13.375H9.00037C9.89783 13.375 10.6254 14.1025 10.6254 15V20C10.6254 20.8975 9.89783 21.625 9.00037 21.625H4.00037C3.1029 21.625 2.37537 20.8975 2.37537 20L2.37537 15ZM4.00037 14.625C3.79326 14.625 3.62537 14.7929 3.62537 15L3.62537 20C3.62537 20.2071 3.79326 20.375 4.00037 20.375H9.00037C9.20747 20.375 9.37537 20.2071 9.37537 20V15C9.37537 14.7929 9.20747 14.625 9.00037 14.625H4.00037Z"
      fill="currentColor"
    />
    <path
      fillRule="evenodd"
      clipRule="evenodd"
      d="M15.0004 13.375C14.1029 13.375 13.3754 14.1025 13.3754 15V20C13.3754 20.8975 14.1029 21.625 15.0004 21.625H20.0004C20.8978 21.625 21.6254 20.8975 21.6254 20L21.6254 15C21.6254 14.1025 20.8978 13.375 20.0004 13.375H15.0004ZM14.6254 15C14.6254 14.7929 14.7933 14.625 15.0004 14.625H20.0004C20.2075 14.625 20.3754 14.7929 20.3754 15L20.3754 20C20.3754 20.2071 20.2075 20.375 20.0004 20.375H15.0004C14.7933 20.375 14.6254 20.2071 14.6254 20V15Z"
      fill="currentColor"
    />
  </>,
  "Miscellaneous",
);

export default function Miscellaneous(props: SvgIconProps) {
  return <MiscellaneousIcon {...props} viewBox="0 0 24 24" fill="none" />;
}
