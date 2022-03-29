import { Link } from "react-router-dom";

const Footer = ({ open, onSend }) => {
  const onClickF = () => {
    console.log("button clicked");
    onSend({});
  };
  return (
    <div class="lc-footer">
      <div class="lc-footer-form">
        <textarea
          aria-label="Write a message…"
          enterKeyHint="send"
          class="lc-footer-form-textarea"
          placeholder="Write a message…"
          document="[object HTMLDocument]"
        ></textarea>
        <div class="lc-footer-form-send">
          <button
            aria-label="Send a message"
            class="lc-footer-form-button"
            onClick={onClickF}
          >
            <svg viewBox="0 0 32 32" class="lc-footer-form-icon">
              <path d="M6.4,5.6l21,9.5c0.5,0.2,0.7,0.8,0.5,1.3c-0.1,0.2-0.3,0.4-0.5,0.5l-21,9.5	c-0.5,0.2-1.1,0-1.3-0.5c-0.1-0.3-0.1-0.6,0-0.8L8.6,18L20.5,16L8.6,14.1L5.1,6.9c-0.2-0.5,0-1.1,0.5-1.3C5.8,5.5,6.1,5.5,6.4,5.6z"></path>
            </svg>
          </button>
        </div>
      </div>
    </div>
  );
};

export default Footer;
