/**
 * Modal form constructor
 *
 * @constructor
 */
function ModalForm(options){

    this.on = false;
    
    this._items = [];
    this._cur_item_idx = 0;
    this._title  = "";
    this._status = "";
    this._text = "";
    this._parent = {};
    this._id = '';
    this._need_restore_parent_on = false;
    this._on_exit_close = false;

    this.options = options;

    this._parse_options(options);

    this._init();
}

ModalForm.prototype._parse_options = function(options){
    if (options){
        for (var prop in options){
            if (options.hasOwnProperty(prop)){
                this["_"+prop] = options[prop];
            }
        }
    }
};

ModalForm.prototype._init = function(){
    this._dom_obj        = create_block_element("modal_form");

    if (this._id){
        this._dom_obj.setAttribute('id', this._id);
    }

    this._title_dom_obj  = create_block_element("title", this._dom_obj);
    this._title_dom_obj.innerHTML = this._title;
    this._status_dom_obj = create_block_element("status", this._dom_obj);

    if (this._text){
        this._text_dom_obj = create_block_element("text", this._dom_obj);
        this._text_dom_obj.innerHTML = this._text;
    }

    this._items_block    = create_block_element("", this._dom_obj);
    this._buttons_block  = create_block_element("buttons", this._dom_obj);
    this.hide();
    //this._bind.call(this);
    this._bind();
};

ModalForm.prototype.show = function(params){

    this.triggerCustomEventListener("before_show", this);

    if (typeof(params) == 'string'){
        var text = params;
    }else if (typeof(params) == 'object'){
        this._parse_options(params);

        if (!params.hasOwnProperty('parent')){
            this._parent = null;
            this._need_restore_parent_on = false;
        }

        if (params.hasOwnProperty('text')){
            text = params.text;
        }
    }

    if (text){
        this.setText(text);
    }

    this._dom_obj.show();
    this.on = true;

    if (this._parent && this._parent.on){
        this._need_restore_parent_on = true;
        this._parent.on = false;
    }else{
        this._need_restore_parent_on = false;
    }

    this.triggerCustomEventListener("show", this);
    this._items[0].focus();
};

ModalForm.prototype.hide = function(){
    this.triggerCustomEventListener("before_hide", this);
    this._items[this._cur_item_idx] && this._items[this._cur_item_idx].blur && this._items[this._cur_item_idx].blur();
    this._dom_obj.hide();
    this.on = false;
    this.reset();
    if (this._need_restore_parent_on){
        this._parent.on = true;
    }
    this.triggerCustomEventListener("hide", this);
};

ModalForm.prototype.reset = function(){
    this._items.map(function(item){
        item && item.reset && item.reset();
    });
    this._cur_item_idx = 0;
};

ModalForm.prototype.destroy = function(){
    this._dom_obj.parentNode.removeChild(this._dom_obj);
};

ModalForm.prototype.addItem = function(item){
    this._items.push(item);

    if (item instanceof ModalFormButton){
        this._buttons_block.appendChild(item.getDomElement.call(item));
    }else{
        this._items_block.appendChild(item.getDomElement.call(item));
    }
};

ModalForm.prototype._setActiveItem = function(){
    this._items[this._cur_item_idx] && this._items[this._cur_item_idx].focus && this._items[this._cur_item_idx].focus();
};

ModalForm.prototype._setPassiveItem = function(){
    this._items[this._cur_item_idx] && this._items[this._cur_item_idx].blur && this._items[this._cur_item_idx].blur();
};

ModalForm.prototype._changeFocus = function(dir){

    this._setPassiveItem();

    if (dir > 0){
        if (this._cur_item_idx < this._items.length - 1){
            this._cur_item_idx++;
        }else{
            //this._cur_item_idx = 0;
        }
    }else{
        if (this._cur_item_idx > 0){
            this._cur_item_idx--;
        }else{
            //this._cur_item_idx = this._items.length - 1;
        }
    }

    this._setActiveItem();
};

ModalForm.prototype.getItemByName = function(name){

    var search = this._items.filter(function(item){
        if (item.getName() == name){
            return true;
        }
    });

    if (!search){
        return null;
    }

    return search[0]; 
};

ModalForm.prototype.setStatus = function(status){

    this._status = status;
    this._status_dom_obj.innerHTML = status;
};

ModalForm.prototype.resetStatus = function(){

    _debug("this._status", this._status);

    if (this._status != ""){
        this._status_dom_obj.innerHTML = "";
        this._status = "";
    }
};

ModalForm.prototype._bind = function(){

    (function(dir){

        if (this._items[this._cur_item_idx] instanceof ModalFormDateTimeSelect && this._items[this._cur_item_idx].inEditMode()){
            this._items[this._cur_item_idx].verticalShift(dir > 0 ? -1 : 1);
        }else{
            this._changeFocus(dir);
        }

    }).bind(key.DOWN, this,  1).bind(key.UP,   this, -1);

    (function(){
        if (this._items[this._cur_item_idx] instanceof ModalFormButton){
            this._changeFocus(-1);
        }else if (this._items[this._cur_item_idx] instanceof ModalFormSelect || this._items[this._cur_item_idx] instanceof ModalFormDateTimeSelect){
            this._items[this._cur_item_idx].shift(-1);
        }
    }).bind(key.LEFT, this);

    (function(){
        if (this._items[this._cur_item_idx] instanceof ModalFormButton){
            this._changeFocus(1);
        }else if (this._items[this._cur_item_idx] instanceof ModalFormSelect || this._items[this._cur_item_idx] instanceof ModalFormDateTimeSelect){
            this._items[this._cur_item_idx].shift(1);
        }
    }).bind(key.RIGHT, this);

    (function(){
        if (this._items[this._cur_item_idx] instanceof ModalFormInput){
            stb.ShowVirtualKeyboard();
        }else if (this._items[this._cur_item_idx] instanceof ModalFormButton){
            this._items[this._cur_item_idx].action();
        }else if (this._items[this._cur_item_idx] instanceof ModalFormDateTimeSelect){
            this._items[this._cur_item_idx].toggleEditMode();
        }
    }).bind(key.OK, this).bind(key.KEYBOARD, this);

    (function(){
        if (this._items[this._cur_item_idx] instanceof ModalFormDateTimeSelect && this._items[this._cur_item_idx].inEditMode()){
            this._items[this._cur_item_idx].disableEditMode();
        }else if(this._on_exit_close){
            this.hide();
        }
    }).bind(key.EXIT, this);

    (function(){}).bind(key.TV, this);
};

ModalForm.prototype.enableOnExitClose = function(){
    this._on_exit_close = true;
};

ModalForm.prototype.getTitleDomObj = function(){
    return this._title_dom_obj;
};

ModalForm.prototype.getButtonsBlockDomObj = function(){
    return this._buttons_block;
};

ModalForm.prototype.getTextDomObj = function(){
    return this._text_dom_obj;
};

ModalForm.prototype.setText = function(text){
    this._text_dom_obj.innerHTML = text;
};
/* END ModalForm */

/**
 * @constructor
 */
function ModalFormItem(){}

ModalFormItem.prototype.focus = function(){
    this._input_dom_odj && this._input_dom_odj.focus  && this._input_dom_odj.focus();
};

ModalFormItem.prototype.blur = function(){
    this._input_dom_odj && this._input_dom_odj.blur  && this._input_dom_odj.blur();
};

ModalFormItem.prototype.getDomElement = function(){
    return this._item;
};

ModalFormItem.prototype.getName = function(){};

/* END ModalFormItem */

/**
 * Input element
 *
 * @constructor
 * @param {Object} options
 */
function ModalFormInput(options){

    this._name  = "";
    this._type  = "text";
    this._label = "";
    this._value = "";
    this._placeholder = "";
    this._onchange =  function(){};
    this._oninput =  function(){};

    this.options = options;

    if (options){
        for (var prop in options){
            if (options.hasOwnProperty(prop)){
                this["_"+prop] = options[prop];
            }
        }
    }

    this._init();
}

ModalFormInput.prototype = new ModalFormItem();

ModalFormInput.prototype._init = function(){
    this._item = document.createElement("div");
    this._item.setClass("item");
    this._label_dom_obj = create_block_element("label", this._item);
    this._label_dom_obj.innerHTML = this._label;
    this._input_dom_odj = document.createElement("input");
    this._input_dom_odj.setAttribute("type",  this._type);
    this._input_dom_odj.setAttribute("value", this._value);
    this._input_dom_odj.setAttribute("placeholder", this._placeholder);
    this._input_dom_odj.onchange = this._onchange;
    this._input_dom_odj.oninput = this._oninput;
    this._item.appendChild(this._input_dom_odj);
};

ModalFormInput.prototype.setValue = function(value){
    return this._input_dom_odj.value = value;
};

ModalFormInput.prototype.getValue = function(){
    return this._input_dom_odj.value;
};

ModalFormInput.prototype.getName = function(){
    return this._name;
};

ModalFormInput.prototype.reset = function(){
    this._input_dom_odj.value = this._value;
};
/* END ModalFormInput */

/**
 * Button element
 * 
 * @constructor
 * @param {Object} options
 */
function ModalFormButton(options){
    this._value = "";
    this._name = "";
    this._onclick  = function(){};

    if (options){
        for (var prop in options){
            if (options.hasOwnProperty(prop)){
                this["_"+prop] = options[prop];
            }
        }
    }

    this._init();
}

ModalFormButton.prototype = new ModalFormItem();

ModalFormButton.prototype._init = function(){
    this._input_dom_odj = document.createElement("input");
    this._input_dom_odj.setAttribute("type",  "button");
    this._input_dom_odj.setAttribute("value", this._value);
};

ModalFormButton.prototype.action = function(){
    this._onclick && this._onclick();
};

ModalFormButton.prototype.getDomElement = function(){
    return this._input_dom_odj;
};

ModalFormButton.prototype.setValue = function(value){
    this._value = value;
    this._input_dom_odj.setAttribute("value", this._value);
};

ModalFormButton.prototype.getName = function(){
    return this._name;
};

/* END ModalFormButton*/

/**
 * Select element
 *
 * @constructor
 * @param {Object} options
 */
function ModalFormSelect(options){
    this._name  = "";
    this._label = "";
    this._default = "";
    this._options = [];
    this._cur_idx = 0;
    this._onchange =  function(){};

    this.options = options;

    if (options){
        for (var prop in options){
            if (options.hasOwnProperty(prop)){
                this["_"+prop] = options[prop];
            }
        }
    }

    this._init();
}

ModalFormSelect.prototype = new ModalFormItem();

ModalFormSelect.prototype.focus = function(){
    this._input_dom_odj.addClass('active');
    this.update_input();
};

ModalFormSelect.prototype.blur = function(){
    this._input_dom_odj.removeClass('active');
    this.left_arrow.removeClass('active');
    this.update_input();
};

ModalFormSelect.prototype._init = function(){
    this._item = document.createElement("div");
    this._item.setClass("item");
    this._label_dom_obj = create_block_element("label", this._item);
    this._label_dom_obj.innerHTML = this._label;

    var input_container = create_block_element("", this._item);
    input_container.style.float = 'right';

    this.right_arrow = create_block_element("select_arrow", input_container);
    this.right_arrow.innerHTML = '&gt;';

    this._input_dom_odj = document.createElement("input");
    this._input_dom_odj.addClass('form_select');
    this._input_dom_odj.setAttribute("readonly",  "readonly");
    this._input_dom_odj.setAttribute("type",  "text");

    this._input_dom_odj.onchange = this._onchange;
    input_container.appendChild(this._input_dom_odj);

    this.left_arrow = create_block_element("select_arrow", input_container);
    this.left_arrow.innerHTML = '&lt;';

    this.setOptions(this._options);
};

ModalFormSelect.prototype.setOptions = function(options){

    this._options = options || [];

    this._cur_idx = this._options.getIdxByVal('selected', true);
    this._cur_idx = this._cur_idx || 0;

    this.update_input();
};

ModalFormSelect.prototype.update_input = function(){
    if (this._options.length > 0){
        this._input_dom_odj.value = this._options[this._cur_idx].text;
    }

    _debug('this._cur_idx', this._cur_idx);
    _debug('this._options', this._options);
    _debug('this._options.length', this._options.length);

    this.left_arrow.removeClass('active');
    this.right_arrow.removeClass('active');

    if (this._cur_idx == 0){
        this.left_arrow.removeClass('active');
    }else{
        this.left_arrow.addClass('active');
    }

    if (this._options.length == 0 || this._cur_idx >= this._options.length || this._cur_idx == this._options.length-1){
        this.right_arrow.removeClass('active');
    }else{
        this.right_arrow.addClass('active');
    }

    _debug('this.left_arrow.className', this.left_arrow.className);
    _debug('this.right_arrow.className', this.right_arrow.className);
};

ModalFormSelect.prototype.shift = function(dir){

    if (dir > 0){
        if (this._cur_idx < this._options.length - 1){
            this._cur_idx++;
        }
    }else{
        if (this._cur_idx > 0){
            this._cur_idx--;
        }
    }

    this.update_input();
};

ModalFormSelect.prototype.getValue = function(){

    if (this._options.length == 0){
        return null;
    }

    return this._options[this._cur_idx].value;
};

ModalFormSelect.prototype.getText = function(){

    if (this._options.length == 0){
        return null;
    }

    return this._options[this._cur_idx].text;
};

ModalFormSelect.prototype.getName = function(){
    return this._name;
};

/* END ModalFormSelect*/

/**
 * Select DateTimeSelect
 *
 * @constructor
 * @param {Object} options
 */

function ModalFormDateTimeSelect(options){
    this._name  = "";
    this._label = "";
    this._default = "now";
    this._onchange =  function(){};
    this._onset =  function(){};

    this._active_time = true;
    this._edit_mode = false;
    this._only_time = false;

    this._max_time = "23:59";
    this._max_date = "31.12.2037";

    this._section_idx = 0;

    this.options = options;

    if (options){
        for (var prop in options){
            if (options.hasOwnProperty(prop)){
                this["_"+prop] = options[prop];
            }
        }
    }

    this._init();
}

ModalFormDateTimeSelect.prototype = new ModalFormItem();

ModalFormDateTimeSelect.prototype.focus = function(){
    if (this._time_dom_odj && this._time_dom_odj.addClass){
        this._focus_time();
    }
};

ModalFormDateTimeSelect.prototype._focus_time = function(){
    this._blurDate();
    this._active_time = true;
    if (this._time_dom_odj && this._time_dom_odj.addClass){
        this._time_dom_odj.addClass('active');
    }
};

ModalFormDateTimeSelect.prototype._focus_date = function(){
    this._blurTime();
    this._active_time = false;
    if (this._date_dom_odj && this._date_dom_odj.addClass){
        this._date_dom_odj.addClass('active');
    }
};

ModalFormDateTimeSelect.prototype.blur = function(){
    this.disableEditMode();
    this._blurTime();
    this._blurDate();
    this._active_time = true;
};

ModalFormDateTimeSelect.prototype._blurTime = function(){
    if (this._time_dom_odj && this._time_dom_odj.addClass){
        this._time_dom_odj.removeClass('active');
    }
};

ModalFormDateTimeSelect.prototype._blurDate = function(){
    if (this._date_dom_odj && this._date_dom_odj.addClass){
        this._date_dom_odj.removeClass('active');
    }
};

ModalFormDateTimeSelect.prototype._init = function(){

    this._item = document.createElement("div");
    this._item.setClass("item");
    this._label_dom_obj = create_block_element("label", this._item);
    this._label_dom_obj.innerHTML = this._label;

    var container = create_block_element("fixed_container", this._item);

    this._time_dom_odj = create_block_element('form_time', container);
    this._time_dom_odj.innerHTML = '00:00';

    if (!this._only_time){
        this._date_dom_odj = create_block_element('form_date', container);
        this._date_dom_odj.innerHTML = '00.00.0000';
    }
};

ModalFormDateTimeSelect.prototype.shift = function(dir){

    if (!this._edit_mode && !this._only_time){
        if (dir > 0){
            if (this._active_time){
                this._focus_date();
            }
        }else{
            if (!this._active_time){
                this._focus_time();
            }
        }
    }else if (this._edit_mode){
        if (dir > 0){

            var total_sections = this._active_time ? 2 : 3;

            if (this._section_idx < total_sections-1){
                this._section_idx++;
            }

        }else{
            if (this._section_idx > 0){
                this._section_idx--;
            }
        }
        this._setActiveSection();
    }
};

ModalFormDateTimeSelect.prototype._setActiveSection = function(){

    var separator = this._active_time ? ":" : ".";

    var input = this._active_time ? this._time_dom_odj : this._date_dom_odj;

    var sections = input.innerHTML.split(separator);

    var self = this;

    sections = sections.map(function(section, idx){
        section = section.replace(/<.*?>/g, '');

        if (idx == self._section_idx){
            section = '<span class="highlight">' + section + '</span>';
        }

        return section;
    });

    input.innerHTML = sections.join(separator);
};

ModalFormDateTimeSelect.prototype._disableSections = function(){

    this._section_idx = -1;
    this._setActiveSection();
};

ModalFormDateTimeSelect.prototype.verticalShift = function(dir){

    var separator = this._active_time ? ":" : ".";

    var input = this._active_time ? this._time_dom_odj : this._date_dom_odj;

    var sections = input.innerHTML.split(separator);

    if (this._active_time){
        var max_map = this._max_time.split(':').map(function(part, idx){
            part = parseInt(part, 10);
            if (idx == 1 && part == 0){
                part = 59;
            }
            return part;
        });
    }else{
        max_map = this._max_date.split('.').map(function(part){
            return parseInt(part, 10);
        });
    }

    var value = parseInt(sections[this._section_idx].replace(/<.*?>/g, ''), 10);

    var min_value = this._section_idx == 2 ? 1900 + new Date().getYear() : 0;

    if (dir > 0){
        if (value < max_map[this._section_idx]){
            value++;
        }else{
            value = min_value;
        }
    }else{
        if (value > min_value){
            value--;
        }else{
            if (this._section_idx != 2){
                value = max_map[this._section_idx];
            }
        }
    }

    if (value < 10){
        value = '0'+value;
    }

    var self = this;

    sections = sections.map(function(section, idx){
        section = section.replace(/<.*?>/g, '');

        if (idx == self._section_idx){
            section = '<span class="highlight">' + value + '</span>';
        }

        return section;
    });

    input.innerHTML = sections.join(separator);
};

ModalFormDateTimeSelect.prototype.inEditMode = function(){
    return this._edit_mode
};

ModalFormDateTimeSelect.prototype.enableEditMode = function(){
    if (this._edit_mode){
        return;
    }

    this._edit_mode = true;

    if (this._active_time){
        this._time_dom_odj.addClass('edit');
    }else{
        this._date_dom_odj.addClass('edit');
    }

    this._section_idx = 0;
    this._setActiveSection();
};

ModalFormDateTimeSelect.prototype.disableEditMode = function(){
    if (!this._edit_mode){
        return;
    }

    this._edit_mode = false;
    if (this._active_time){
        this._time_dom_odj.removeClass('edit');
    }else{
        this._date_dom_odj.removeClass('edit');
    }

    this._disableSections();

    this._onset && this._onset(this.getValue());
};

ModalFormDateTimeSelect.prototype.toggleEditMode = function(){
    if (this._edit_mode){
        this.disableEditMode();
    }else{
        this.enableEditMode();
    }
};

ModalFormDateTimeSelect.prototype.setTime = function(time){
    if (time == 0){
        this._time_dom_odj.innerHTML = '00:00';
    }else if (typeof(time) == 'number'){

        var h = Math.floor(time/3600);
        var m = Math.floor((time - (h*3600)) / 60);
        var time_str = '';

        time_str += this._formatXX(h)+':';

        time_str += this._formatXX(m);

        this._time_dom_odj.innerHTML = time_str;
    }
};

ModalFormDateTimeSelect.prototype.setValue = function(date){
    if (date == 'now'){
        date = new Date();
    }else if (this._only_time){
        this._time_dom_odj.innerHTML = date;
    }else if (typeof(date) == 'string' || typeof(date) == 'number'){
        date = new Date(date);
    }else{
        throw new Error('Unsupported date format');
    }

    if (this._time_dom_odj){
        this._time_dom_odj.innerHTML = this._formatXX(date.getHours())+':'+this._formatXX(date.getMinutes());
    }

    if (this._date_dom_odj){
        this._date_dom_odj.innerHTML = this._formatXX(date.getDate())+'.'+this._formatXX(date.getMonth()+1)+'.'+(1900 + date.getYear());
    }
};

ModalFormDateTimeSelect.prototype.getValue = function(){
    var value = '';

    if (this._date_dom_odj){
        value += this._date_dom_odj.innerHTML;
    }

    if (this._time_dom_odj){

        if (value){
            value += ' ';
        }

        value += this._time_dom_odj.innerHTML;
    }

    return value;
};

/**
 *
 * @return {Date}
 */
ModalFormDateTimeSelect.prototype.getDateValue = function(){

    var date_items = this._date_dom_odj.innerHTML.split('.');

    var time_items = this._time_dom_odj.innerHTML.split(':');

    _debug('new Date', parseInt(date_items[2], 10),
        parseInt(date_items[1], 10),
        parseInt(date_items[0], 10) - 1,
        parseInt(time_items[0], 10),
        parseInt(time_items[1], 10));

    var date = new Date(
        parseInt(date_items[2], 10),
        parseInt(date_items[1], 10) - 1,
        parseInt(date_items[0], 10),
        parseInt(time_items[0], 10),
        parseInt(time_items[1], 10)
    );

    _debug('date', date);

    return date;
};

ModalFormDateTimeSelect.prototype.getName = function(){
    return this._name;
};

ModalFormDateTimeSelect.prototype._formatXX = function(value){
    if (value < 10){
        value = '0'+value;
    }
    return value;
};

loader.next();