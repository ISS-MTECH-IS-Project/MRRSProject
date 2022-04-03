import { BiSend } from "react-icons/bi";
const Footer = ({ open, onSend }) => {
  const onClickF = () => {
    console.log("button clicked");
    onSend({});
  };
  return (
    <div className="lc-footer">
      <div className="lc-footer-form">
        <textarea
          aria-label="Write a message…"
          enterKeyHint="send"
          className="lc-footer-form-textarea"
          placeholder="Write a message…"
          document="[object HTMLDocument]"
        ></textarea>
        <div className="lc-footer-form-send">
          <button
            aria-label="Send a message"
            className="lc-footer-form-button"
            onClick={onClickF}
          >
            <BiSend />
          </button>
        </div>
      </div>
    </div>
  );
};

export default Footer;
