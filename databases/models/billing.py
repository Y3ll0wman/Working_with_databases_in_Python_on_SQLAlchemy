from sqlalchemy import Column, Date, DECIMAL, DateTime, Enum, TIMESTAMP, Float, ForeignKey, Index, String, Text, Time, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT, BIGINT, SMALLINT, MEDIUMTEXT, MEDIUMINT, MEDIUMBLOB, VARCHAR
from sqlalchemy.orm import relationship, DeclarativeBase


class Base(DeclarativeBase):
    pass


class Plans(Base):
    __tablename__ = 'plans'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(60))
    rate = Column(DECIMAL(15, 8))
    wm_rate = Column(Float, nullable=False, server_default=text("'0'"))
    rate_daily = Column(DECIMAL(15, 8), nullable=False, server_default=text("'0.00000000'"))
    rate_hyearly = Column(DECIMAL(15, 8), nullable=False, server_default=text("'0.00000000'"))
    rate_yearly = Column(DECIMAL(15, 8), nullable=False, server_default=text("'0.00000000'"))
    quota = Column(Float, server_default=text("'0'"))
    inode_quota = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    maxftp = Column(INTEGER(11), server_default=text("'0'"))
    maxsites = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    maxmysql = Column(INTEGER(11), server_default=text("'0'"))
    maxpop = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    maxlist = Column(INTEGER(11), server_default=text("'0'"))
    maxpark = Column(String(16), server_default=text("'unlimited'"))
    maxjabber = Column(INTEGER(11), nullable=False, server_default=text("'100'"))
    mail_limit = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    cp_mailman = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    cp_webmail = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    cp_domains = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    cp_subdomains = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    cp_sites = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    cp_ftp = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    cp_fileman = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    cp_mysql = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    cp_logmanager = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    cp_crontab = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    cp_nettools = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    cp_dns = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    cp_backup = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    cp_balance = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    cp_support = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    cp_cms = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    cp_server = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    cp_users = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    cp_catalog = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    period = Column(Enum('Y', 'M'), index=True, server_default=text("'M'"))
    bonus_regdom = Column(Enum('Y', 'N'), server_default=text("'N'"))
    p_latin = Column(String(255), nullable=False, index=True, server_default=text("''"))
    public = Column(Enum('Y', 'N'), server_default=text("'N'"))
    order = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    like_id = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    dealers = Column(String(2048), nullable=False)
    p_purpose = Column(Enum('real', 'test'), server_default=text("'real'"))
    cp_bonuses = Column(Enum('Y', 'N'), server_default=text("'N'"))
    cp_mysql4 = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    cp_accounts = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    cp_letters = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    cp_help = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    p_type = Column(Enum('virtual', 'vip', 'vps', 'free', 'unlim', 'xen', 'dedic'), nullable=False)
    plan_group_id = Column(ForeignKey('plan_groups.id'), index=True)
    is_closed = Column(TINYINT(1), nullable=False, server_default=text("'0'"))

    plan_group = relationship('PlanGroups', primaryjoin='Plans.plan_group_id == PlanGroups.id')


class Invoices(Base):
    __tablename__ = 'invoices'
    __table_args__ = (
        Index('customer_id', 'customer_id', 'payer_handler', 'payment_type_id', 'i_contractor'),
        Index('i_contractor_2', 'i_contractor', 'status', 'i_month', 'i_year'),
        Index('i_contractor_3', 'i_contractor', 'i_month', 'i_year'),
        Index('i_contractor', 'i_contractor', 'status'),
        Index('payment_type_id_status', 'payment_type_id', 'status')
    )

    num = Column(INTEGER(11), primary_key=True)
    domain = Column(String(50))
    customer_id = Column(String(20))
    money = Column(Float(8))
    status = Column(Enum('new', 'paid', 'storned'), nullable=False, server_default=text("'new'"))
    hosting = Column(Enum('Y', 'N'))
    regdom = Column(Enum('Y', 'N'))
    contract = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    server = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    currency = Column(Enum('RUB', 'YND', 'CC', 'MM'))
    payer_handler = Column(INTEGER(8), index=True)
    actes_payer = Column(INTEGER(8), nullable=False)
    idate = Column(Date, index=True)
    itime = Column(Time, nullable=False, server_default=text("'00:00:00'"))
    pdate = Column(DateTime, index=True)
    chksum = Column(String(40), nullable=False, index=True, server_default=text("''"))
    payment_type_id = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    i_desc = Column(String(30720), nullable=False)
    cardnumber = Column(String(16), nullable=False, server_default=text("''"))
    external_number = Column(String(20), nullable=False, index=True, server_default=text("''"))
    i_contractor = Column(Enum('timeweb', 'centertime'), nullable=False, server_default=text("'timeweb'"))
    i_month = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    i_year = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    vds_id = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    autopay = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    custom_description = Column(Text, comment='Optional text to display in printed PDF instead of i_desc.')
    source = Column(String(255), comment='See rbac.app_keys.app_name')
    nds_rate = Column(INTEGER(11), server_default=text("'20'"), comment='Число -> процентная ставка НДС.\\nNULL - > без НДС.\\n\\nШпаргалка эталонного расчета сумм для документов:\\n#Сумма счета\\ntotal = round(money, 2)\\n#Сумма НДС\\nnds = round(total * nds_rate / (100 + nds_rate)), 2)\\n#Сумма без учета НДС\\nno_nds = round(total - nds, 2)')
    payment_system_id = Column(ForeignKey('payment_systems.id', ondelete='SET NULL'), index=True, comment='Идентификатор платежной системы в billing.payment_systems')
    payment_system_merchant_id = Column(INTEGER(11), comment='ID магазина в billing.payment_system_merchants')
    company_info_id = Column(ForeignKey('company_info.id'), index=True, server_default=text("'5'"), comment='Связан с company_info.id')

    company_info = relationship('CompanyInfo')
    payment_system = relationship('PaymentSystems')


class PaymentSystems(Base):
    __tablename__ = 'payment_systems'
    __table_args__ = {'comment': 'Таблица типов платежных систем'}

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(40), nullable=False)


class ServerCapacity(Plans):
    __tablename__ = 'server_capacity'

    plan_id = Column(ForeignKey('plans.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    max_cpu = Column(BIGINT(20))
    max_mysql = Column(BIGINT(20))


class LettersHtmlTemplatesImages(Base):
    __tablename__ = 'letters_html_templates_images'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    content = Column(MEDIUMBLOB)


class DailyCharges(Base):
    __tablename__ = 'daily_charges'

    id = Column(INTEGER(10), primary_key=True)
    cust_login = Column(String(20), nullable=False, index=True)
    vds_id = Column(INTEGER(11), nullable=False)
    date = Column(DateTime, nullable=False, index=True)
    type = Column(Enum('pereodical', 'once', 'incom', 'periodical'), nullable=False)
    summ = Column(Float, nullable=False)
    descr = Column(String(255), nullable=False)
    invoice = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    description_data = Column(String(355))


class Vhosts(Base):
    __tablename__ = 'vhosts'
    __table_args__ = (
        Index('fqdn_2', 'fqdn', 'subdomain', unique=True),
        Index('customer_id_2', 'customer_id', 'subdomain')
    )

    id = Column(INTEGER(11), primary_key=True)
    customer_id = Column(String(20), index=True, server_default=text("''"))
    fqdn = Column(String(255), index=True, server_default=text("''"))
    server = Column(String(20), index=True, server_default=text("''"))
    subdomain = Column(String(100), index=True, server_default=text("''"))
    site_id = Column(INTEGER(11), nullable=False, index=True, server_default=text("'0'"))
    serial = Column(BIGINT(20), nullable=False, index=True, server_default=text("'0'"))
    error_log = Column(Enum('Y', 'N'), nullable=False, index=True, server_default=text("'N'"))
    custom_log = Column(Enum('Y', 'N'), nullable=False, index=True, server_default=text("'N'"))
    awstats = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    ip_id = Column(INTEGER(11), nullable=False, index=True, server_default=text("'0'"))
    v_date = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    v_primary = Column(Enum('Y', 'N'), nullable=False, index=True, server_default=text("'N'"))
    webserver = Column(Enum('apache', 'nginx'), nullable=False, index=True, server_default=text("'apache'"))
    advanced_settings = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    protection = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    idn_name = Column(VARCHAR(255), nullable=False, index=True, server_default=text("''"))
    expiration = Column(Date, nullable=False, index=True, server_default=text("'0000-00-00'"))
    ddos = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    blocked = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    vds_id = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    our_domain = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    whois_expiration = Column(Date, nullable=False, server_default=text("'0000-00-00'"))
    is_system = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    certificate_id = Column(INTEGER(11), index=True, comment='certificate.id установленного SSL-сертификата')
    ssl_check_file = Column(String(255), comment='Наименование файла для проверки SSL-сертификата')
    ssl_check_key = Column(String(255), comment='Ключ для проверки SSL-сертификата')
    is_premium = Column(TINYINT(1), nullable=False, server_default=text("'0'"), comment='Является ли домен премиальным')
    bind_to_constructor_site = Column(TINYINT(1), nullable=False, server_default=text("'0'"), comment='Признак привязки домена к сайту на конструкторе')
    reversed_fqdn = Column(String(255), nullable=False, index=True, comment='Реверсивное значение fqdn для поиска по шаблону')
    tld_name = Column(String(255), nullable=False, index=True, comment='Домен верхнего уровня')
    expiration_last_update = Column(Date, nullable=False, server_default=text("'0000-00-00'"), comment='Дата последней синхронизации expiration с информацией провайдера')
    provider_support = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"), comment='Существование домена у провайдера - статус временный и используется для дальнейшего изменения our_domain')


class Certificate(Base):
    __tablename__ = 'certificate'

    id = Column(INTEGER(11), primary_key=True)
    storage_id = Column(INTEGER(11), nullable=False, comment='system.ssl_storage.id - сертификат и ключ в хранилище')
    customer_id = Column(String(20), nullable=False, index=True, comment='billing.customers.cust_login - логин аккаунта пользователя')
    fqdn = Column(String(255), nullable=False, index=True, comment='имя домена, для которого выпущен SSL-сертификат')
    end_date = Column(Date, nullable=False, comment='дата окончания действия SSL-сертификата')
    email = Column(String(255), comment='email для верификации SSL-сертификата')
    type_id = Column(INTEGER(11), comment='billing.service_types.id - тип SSL-сертификата')
    person_id = Column(INTEGER(11), comment='billing.persons.id - персона, на данные которой был выпущен SSL-сертификат')
    free_ip = Column(String(15), comment='IP-адрес, выданный в комплекте с сертификатом')
    autoprolong = Column(TINYINT(1), nullable=False, server_default=text("'0'"), comment='Автоматически продлевать сертификат под конец срока действия')
    deleted = Column(TINYINT(1), nullable=False, server_default=text("'0'"), comment='Сертификат удален')
    ability_autoprolong = Column(TINYINT(1), nullable=False, server_default=text("'1'"))


class CompanyInfo(Base):
    __tablename__ = 'company_info'

    id = Column(INTEGER(10), primary_key=True)
    company = Column(String(45), nullable=False)
    name_ru = Column(String(32), nullable=False)
    name_de = Column(String(32), nullable=False)
    name_en = Column(String(32), nullable=False)
    org_address = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    mailing_address = Column(String(255), nullable=False)
    phone = Column(String(200), nullable=False, server_default=text("''"), comment='Номера телефонов компании')
    inn = Column(String(12), nullable=False)
    kpp = Column(String(9), nullable=False)
    ogrn = Column(String(13), nullable=False)
    account = Column(String(60), nullable=False)
    cor_account = Column(String(60), nullable=False)
    bank = Column(String(255), nullable=False)
    bik = Column(String(9), nullable=False)
    okved = Column(String(32), nullable=False)
    license = Column(String(16))
    actuality_date = Column(Date, nullable=False)
    vat = Column(INTEGER(2), server_default=text("'20'"), comment='Налог на добавленную стоимость')
    is_active = Column(TINYINT(1), server_default=text("'0'"), comment='Признак текущей организации')
    billing_email = Column(String(255), nullable=False, comment='Почтовый ящик для информации о платежах')
    sno = Column(String(16), nullable=False, comment='Тип системы налогообложения')


class CustomTagsList(Base):
    __tablename__ = 'custom_tags_list'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255), unique=True)
    comments = Column(Text)
    tag_group = Column(String(255))


class DomainProviders(Base):
    __tablename__ = 'domain_providers'

    provider_tag = Column(String(255), primary_key=True)


class LettersBasementBlocks(Base):
    __tablename__ = 'letters_basement_blocks'

    id = Column(INTEGER(11), primary_key=True)
    block_name = Column(String(255), nullable=False, unique=True)
    description = Column(String(255))
    html = Column(Text)


class LettersHtmlTemplates(Base):
    __tablename__ = 'letters_html_templates'

    id = Column(INTEGER(11), primary_key=True)
    template_name = Column(String(200), nullable=False, unique=True)
    description = Column(String(200))
    html = Column(Text)


class PlanGroups(Base):
    __tablename__ = 'plan_groups'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(20), nullable=False)
    reg_server_id = Column(ForeignKey('servers.id'), index=True)
    reg_org_server_id = Column(ForeignKey('servers.id'), index=True)
    dont_reduce_days = Column(INTEGER(11))
    letter_id = Column(ForeignKey('letters.id'), index=True)
    default_tld_id = Column(ForeignKey('tld.id'), index=True)
    test_plan_id = Column(ForeignKey('plans.id'), index=True)
    user_type = Column(String(16))
    followup_letter_id = Column(ForeignKey('letters.id', ondelete='SET NULL', onupdate='CASCADE'), index=True)
    followup_letter_sent_tag = Column(ForeignKey('custom_tags_list.id', ondelete='SET NULL', onupdate='CASCADE'), index=True, comment='If record with a certain EMAIL and this TAG_ID exists in billing.custom_tags,\\nthen the followup_letter had already been sent to mentioned EMAIL.')

    default_tld = relationship('Tld')
    followup_letter = relationship('Letters', primaryjoin='PlanGroups.followup_letter_id == Letters.id')
    custom_tags_list = relationship('CustomTagsList')
    letter = relationship('Letters', primaryjoin='PlanGroups.letter_id == Letters.id')
    reg_org_server = relationship('Servers', primaryjoin='PlanGroups.reg_org_server_id == Servers.id')
    reg_server = relationship('Servers', primaryjoin='PlanGroups.reg_server_id == Servers.id')
    test_plan = relationship('Plans', primaryjoin='PlanGroups.test_plan_id == Plans.id')


class Servers(Base):
    __tablename__ = 'servers'
    __table_args__ = (
        Index('backup', 'backup', 'backup_scheme'),
    )

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(30), index=True)
    purpose = Column(Enum('hosting', 'service', 'colocation', 'noadm', 'vps', 'storage'), nullable=False, server_default=text("'hosting'"))
    server_profile_id = Column(INTEGER(11), nullable=False)
    bday = Column(String(20), nullable=False)
    mac = Column(String(100), nullable=False, server_default=text("''"), comment='MAC-адрес первого интерфейса, исключительно для физических серверов')
    ip = Column(String(20), server_default=text("''"))
    ipv6 = Column(String(255), nullable=False, server_default=text("''"))
    local_ip = Column(String(20), comment='локальный IP-адрес, исключительно для служебных серверов')
    backup_ip = Column(String(16), nullable=False)
    nginx_ip = Column(String(20), nullable=False, server_default=text("''"))
    info_os = Column(String(30), nullable=False, server_default=text("'Linux'"))
    info_kernel = Column(String(10), nullable=False, server_default=text("'Linux'"))
    info_distr = Column(String(30), nullable=False)
    info_distr_release = Column(String(30))
    info_apache = Column(String(30), nullable=False, server_default=text("''"))
    info_mysql = Column(String(30), nullable=False, server_default=text("''"))
    info_perl = Column(String(30), nullable=False, server_default=text("''"))
    info_php = Column(String(30), nullable=False, server_default=text("''"))
    info_python = Column(String(30), nullable=False, server_default=text("''"))
    dealers = Column(MEDIUMTEXT, nullable=False)
    backup = Column(String(30), nullable=False, server_default=text("'backup0'"))
    backup_copies = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    backup_scheme = Column(Enum('simple', 'advanced', 'drbd_sync', 'lvm', 'rsync_storage', 'rsync_local', 'drbd_thin', 'drbd_heavy', 'zfs'))
    scheme_info = Column(String(255), nullable=False, server_default=text("''"))
    backup_dirs = Column(String(1024), nullable=False, server_default=text("'/var/lib/mysql,/etc,/home'"))
    cs = Column(SMALLINT(5), nullable=False, index=True, server_default=text("'0'"))
    backup_result = Column(MEDIUMTEXT, nullable=False)
    port = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    switch = Column(INTEGER(11))
    switch_port = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    switch_port_1 = Column(INTEGER(11), nullable=False, server_default=text("'-1'"))
    virtual = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    hostnode = Column(String(20), nullable=False, server_default=text("''"))
    owner = Column(String(20), nullable=False, index=True, server_default=text("''"))
    cacti_id = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    config_id = Column(INTEGER(11), nullable=False, index=True, server_default=text("'0'"))
    location = Column(INTEGER(11), nullable=False, index=True, server_default=text("'1'"))
    monitor_http = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    monitor_mysql = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    monitor_ftp = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    monitor_root = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    monitor_home = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    monitor_backup = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    monitor_smtp = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    monitor_pop3 = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    monitor_dns = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    apache_config = Column(Enum('singleuser', 'multiuser'), nullable=False, server_default=text("'multiuser'"))
    srv_desc = Column(MEDIUMTEXT, nullable=False)
    dump_innodb = Column(Enum('Y', 'N'), nullable=False, server_default=text("'Y'"))
    multiapache = Column(Enum('Y', 'N'), nullable=False, server_default=text("'Y'"))
    boxnr = Column(String(15), nullable=False, index=True, server_default=text("'0'"))
    pdu_desc = Column(MEDIUMTEXT, nullable=False)
    kvm_desc = Column(MEDIUMTEXT, nullable=False)
    multiusers = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    vlan = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    transfer_backup = Column(String(20), nullable=False)
    fastapache = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    pdu_id = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    kvm_id = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    mysql_maxconnections = Column(INTEGER(11), nullable=False, server_default=text("'60'"))
    mysql_encoding = Column(String(10), nullable=False, server_default=text("''"))
    max_users = Column(MEDIUMINT(9), nullable=False, server_default=text("'0'"))
    ipv6_ready = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    description = Column(MEDIUMTEXT, nullable=False)
    apache_scheme = Column(Enum('shared', 'dedicated'), server_default=text("'shared'"))
    opaqueref = Column(String(100), nullable=False)
    type_os = Column(String(10), nullable=False)
    info_os_v = Column(String(10), nullable=False)
    alternate_php = Column(String(32), nullable=False, server_default=text("'4'"))
    info_os_n = Column(String(15), nullable=False)
    user_caption = Column(String(255), nullable=False)
    xen_units = Column(INTEGER(11), nullable=False, server_default=text("'1'"))
    xen_ram = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    xen_cpu = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    bandwidth = Column(INTEGER(11), nullable=False, server_default=text("'100'"))
    control_pane = Column(String(255), nullable=False, server_default=text("''"))
    server_balance = Column(Float, server_default=text("'0'"))
    phone = Column(String(32), nullable=False)
    code = Column(String(16), nullable=False)
    phone_confirmed = Column(Enum('N', 'Y'), nullable=False)
    sms_fulltime_vds = Column(Enum('N', 'Y'), nullable=False)
    sms_account_block_vds = Column(Enum('N', 'Y'), nullable=False)
    sms_money_over_vds = Column(Enum('N', 'Y'), nullable=False)
    sms_closed_invoice_vds = Column(Enum('N', 'Y'), nullable=False)
    sms_testperiod_end_vds = Column(Enum('N', 'Y'), nullable=False)
    sms_period_start_vds = Column(String(32), nullable=False)
    sms_period_end_vds = Column(String(32), nullable=False)
    sms_domains_delegation_ends = Column(Enum('Y', 'N'), nullable=False)
    sms_recurrent_payment = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    xenpool = Column(String(32), nullable=False)
    vnc_pass = Column(String(32), nullable=False)
    ipmi_ip = Column(String(20), unique=True)
    ipmi_admin_login = Column(String(255), nullable=False)
    ipmi_admin_pass = Column(String(255), nullable=False)
    ipmi_operator_login = Column(String(255), nullable=False)
    ipmi_operator_pass = Column(String(255), nullable=False)
    descr = Column(String(255), nullable=False)
    cost = Column(INTEGER(11), nullable=False)
    units_limit = Column(String(10), nullable=False)
    discount_percent = Column(INTEGER(3), nullable=False)
    discount_end = Column(Date, nullable=False)
    memory_zone = Column(INTEGER(1), nullable=False, server_default=text("'0'"))
    vds_boot = Column(Enum('std', 'single', 'cd'), nullable=False, server_default=text("'std'"))
    quarantine = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    dont_reduce_hours = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    user_creater = Column(String(100), nullable=False)
    create_date = Column(DateTime, nullable=False)
    in_work_date = Column(DateTime, nullable=False)
    install = Column(Enum('unknown', 'new', 'install_os', 'install_puppet', 'install_drbd', 'installed', 'done'), nullable=False, index=True, server_default=text("'new'"), comment='Hosting server installation status')
    disks_type = Column(Enum('SATA', 'SSD', 'SSD_RAID5'), nullable=False)
    mysql_total = Column(INTEGER(11), nullable=False)
    mysql_used = Column(INTEGER(11), nullable=False)
    home_total = Column(INTEGER(11), nullable=False)
    home_used = Column(INTEGER(11), nullable=False)
    average_LA = Column(Float(6), nullable=False)
    num_customers = Column(INTEGER(11), nullable=False)
    usage_percent = Column(INTEGER(11), nullable=False)
    usage_limiting_factor = Column(Enum('mysql', 'home', 'LA', 'num_customers'))
    customers_capacity = Column(INTEGER(11), nullable=False)
    latest_usage_report = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    pp_preshared_key = Column(String(16), comment='Pre-shared key for Puppet Policy-Based Autosigning')
    puppet_env = Column(String(45), server_default=text("'production'"))
    nproc = Column(INTEGER(3), nullable=False, server_default=text("'0'"), comment='number of cpu cores')
    install_ssh_key = Column(String(4096), nullable=False, server_default=text("''"))
    cs_number = Column(INTEGER(10))
    kvm_vds_vlan = Column(SMALLINT(5), comment='Тегированный vlan, который подаётся на eth1 kvm-ноды. 0 означает старое поведение – нет тегированного трафика, дополнительный порт. Когда будет много vlan, нужно будет создать отдельную таблицу')
    ddos_guard = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"), comment='Признак защиты сети от DDoS')
    uuid_selectel = Column(String(255), comment='UUID сервера в selectel')
    mac_backup = Column(String(20))
    id_sw_backup = Column(INTEGER(11))
    intf_sw_backup = Column(INTEGER(11))
    ipmi_url = Column(String(255), comment='Ссылка на IPMI сервер')


class AccountStatus(Base):
    __tablename__ = 'account_status'
    __table_args__ = (
        Index('plan_id_2', 'plan_id', 'blocked'),
        {'comment': 'Одна из основных таблиц, хранит оперативные данные клиентов'}
    )

    customer_id = Column(String(20), primary_key=True, server_default=text("''"))
    balance = Column(DECIMAL(15, 8), nullable=False, index=True, server_default=text("'0.00000000'"))
    blocked_money = Column(Float, nullable=False, server_default=text("'0'"))
    plan_id = Column(ForeignKey('plans.id', ondelete='SET NULL', onupdate='CASCADE'), index=True)
    last_change_plan = Column(Date, nullable=False)
    order_plan_id = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    blocked = Column(Enum('Y', 'N'), index=True, server_default=text("'Y'"))
    permanent_block = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    last_balance_update = Column(DateTime)
    ssh = Column(Enum('Y', 'N'), server_default=text("'N'"))
    passwd = Column(String(50), nullable=False, server_default=text("''"))
    password_hash = Column(String(255))
    last_pass_changed = Column(DateTime, nullable=False)
    used_space_mysql = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    used_space_mail = Column(BIGINT(20), nullable=False, server_default=text("'0'"))
    want_info_letters = Column(Enum('Y', 'N', 'U'), nullable=False, server_default=text("'U'"))
    want_bill_letters = Column(Enum('Y', 'N', 'U'), nullable=False, index=True, server_default=text("'U'"))
    cp_lang = Column(Enum('ru', 'en', 'de'), nullable=False, server_default=text("'ru'"))
    loading_send = Column(Enum('Y', 'N'), server_default=text("'N'"))
    load_monitoring = Column(Enum('Y', 'N'), nullable=False, index=True, server_default=text("'N'"))
    passpop_show = Column(Enum('Y', 'N'), nullable=False, server_default=text("'Y'"))
    mysql_super_access = Column(Enum('Y', 'N'), server_default=text("'N'"))
    mysql_salt = Column(String(255), nullable=False)
    firewall = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    login_period = Column(String(10), nullable=False)
    ip_verification_code = Column(String(4), nullable=False, index=True, server_default=text("''"))
    first_time = Column(Enum('Y', 'N'), nullable=False, server_default=text("'Y'"))
    cron_mailto = Column(String(255), nullable=False, server_default=text("''"))
    default_backend = Column(Enum('apache', 'nodejs'), nullable=False, server_default=text("'apache'"))
    free_activated = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    would_plan_id = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    action_status = Column(String(255), nullable=False, server_default=text("''"))
    mail_auto_limit = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    personal_manager = Column(String(255), nullable=False)
    test_vds_used = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    god_mode = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    service_vds = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    bill_number = Column(String(16), nullable=False)
    autopay_invoice = Column(INTEGER(11), nullable=False)
    autopay_balance = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    autopay_prolong = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    autopay_last = Column(DateTime, nullable=False)
    autopay_cardinfo = Column(String(200), nullable=False)
    autopay_cardowner = Column(String(200), nullable=False)
    sms_delivery_start = Column(String(5))
    sms_delivery_end = Column(String(5))
    budget = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    sms_auth = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    sms_vds_remove = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    ip_filter = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    country_filter = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    new_panel = Column(Enum('Y', 'N'), nullable=False, server_default=text("'Y'"))
    country = Column(Enum('ru', 'de', 'en'), nullable=False, server_default=text("'ru'"))
    location_server_id = Column(ForeignKey('servers.id', ondelete='SET NULL'), index=True)
    add_backup_copies = Column(TINYINT(3), nullable=False, server_default=text("'0'"), comment='number of additional backup copies')
    cp_login_date = Column(TIMESTAMP)
    should_change_plan = Column(DateTime)
    autopay_failed_attempt = Column(DateTime)
    recv_invoice_copy = Column(Enum('Y', 'N'), nullable=False, server_default=text("'Y'"))
    cp_theme = Column(String(45), nullable=False, server_default=text("'default'"))
    archived = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    cp_allow_expired_pwd = Column(Enum('Y', 'N'), nullable=False, server_default=text("'Y'"))
    last_billed = Column(DateTime, comment="E.g. 2018-07-05 00:00:00 means that daily_reduce must not touch this account until next day's launch (2018-07-06 00:10)")
    plan_payment_period = Column(Enum('M', 'Y', '2Y'), comment='Предоплаченный период (месячный, годовой и т.д.), от которого зависит скидка на выбранном тарифе (plan_id).')
    invoice_auto_creation = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"))
    dedic_order_stage = Column(Enum('not_agreed', 'agreed', 'demounted'))
    first_paid_invoice = Column(INTEGER(10), index=True, comment='Номер первого оплаченного инвойса в жизни клиента.')
    block_date_forecast = Column(DateTime, comment='Прогноз, до какой даты хватает баланса + dont_reduce + взятого отл. платежа.\\nИмеет смысл и обновляется только для активных аккаунтов.')
    country_code = Column(String(2), comment='Страна или группа стран, к которой отнесен пользователь по ISO 3166 Alpha-2')
    current_payment_system_id = Column(ForeignKey('payment_systems.id', ondelete='SET NULL'), index=True, comment='Текущая платежная система')
    company_info_id = Column(ForeignKey('company_info.id'), index=True, server_default=text("'3'"), comment='Связан с company_info.id')
    customer_group = Column(Enum('customers', 'new_customers', 'spammers', 'no_ssh_sftp', 'overloads'), comment='Текущая группа аккаунта')

    company_info = relationship('CompanyInfo')
    current_payment_system = relationship('PaymentSystems')
    location_server = relationship('Servers')
    plan = relationship('Plans')


class Letters(Base):
    __tablename__ = 'letters'
    __table_args__ = (
        Index('uq_name_dealer', 'name', 'dealer', unique=True),
    )

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255), nullable=False)
    letter_text = Column(Text, nullable=False)
    sms_text = Column(Text, nullable=False)
    caption = Column(String(255), nullable=False, server_default=text("''"))
    notice = Column(Text, nullable=False)
    _from = Column('from', String(255), nullable=False, server_default=text("''"))
    subject = Column(String(255), nullable=False, server_default=text("''"))
    dealer = Column(String(20), nullable=False, index=True, server_default=text("'timeweb'"))
    html_text = Column(Text, nullable=False)
    preserve_newlines = Column(TINYINT(1), nullable=False, server_default=text("'1'"), comment='Preserve html_text formatting via changing \\n to <br> and \\n\\n to <p>...</p>\\nUse 0 if you have actual multiline HTML code in html_text.')
    html_greet = Column(String(255), nullable=False, server_default=text("''"))
    execution_script = Column(Text, nullable=False)
    execution_server = Column(String(255), nullable=False)
    html_template = Column(ForeignKey('letters_html_templates.template_name', ondelete='SET NULL', onupdate='CASCADE'), index=True)
    push_text = Column(Text, nullable=False)
    last_update = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    template_engine = Column(Enum('string_replacement', 'jinja2'), nullable=False, server_default=text("'string_replacement'"))
    signature = Column(Text)
    signature_avatar = Column(String(255))
    template_vars = Column(Text)
    basement_block = Column(ForeignKey('letters_basement_blocks.block_name', ondelete='SET NULL', onupdate='CASCADE'), index=True)
    allow_copy_to_wm = Column(TINYINT(1), nullable=False, server_default=text("'0'"), comment='Можно ли дублировать письмо на почту вебмастера (Redmine #78287)')
    company_name = Column(String(45), nullable=False, server_default=text("'timeweb'"))

    letters_basement_blocks = relationship('LettersBasementBlocks')
    letters_html_templates = relationship('LettersHtmlTemplates')


class Tld(Base):
    __tablename__ = 'tld'
    __table_args__ = (
        Index('name', 'name', 'registar', unique=True),
    )

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(40), nullable=False, server_default=text("''"), comment='название доменной зоны')
    price = Column(Float(10), nullable=False, server_default=text("'0.00'"), comment='цена регистрации')
    price_before = Column(Float(10), comment='Cтоимость доменной зоны без скидки')
    reg = Column(Enum('Y', 'N'), server_default=text("'N'"), comment='регистрация разрешена')
    price2 = Column(Float(10), nullable=False, server_default=text("'0.00'"), comment='мусор, не используется')
    prolong = Column(Float(10), nullable=False, server_default=text("'0.00'"), comment='цена продления')
    published = Column(Enum('Y', 'N'), index=True, server_default=text("'Y'"), comment='отображается ли зона на страницах заказа доменов')
    registar = Column(ForeignKey('domain_providers.provider_tag', onupdate='CASCADE'), index=True, comment='через какого регистратора обрабатывается зона')
    group_id = Column(INTEGER(11), nullable=False, comment='идентификатор группы доменной зоны из таблицы billing.tld_groups')
    whois_privacy = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"), comment='статус наличия допуслуги сокрытия данных персоны для домена')
    whois_privacy_price = Column(Float(10), server_default=text("'0.00'"), comment='стоимость допуслуги сокрытие данных персоны для домена')
    whois_privacy_default = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"), comment='Признак что зона имеет сокрытие данных по умолчанию')
    early_renew_period = Column(SMALLINT(6), comment='за сколько дней до конца срока действия уже можно продлевать')
    soon_expire = Column(SMALLINT(6), nullable=False, server_default=text("'60'"), comment='Значение через сколько дней истекает срок продления')
    grace_period = Column(SMALLINT(6), comment='дней преимущественного продления после конца срока действия')
    prolong_enabled = Column(Enum('Y', 'N'), nullable=False, server_default=text("'N'"), comment='продление разрешено')
    transfer = Column(Float(10), nullable=False, comment='Цена переноса домена к нам (в Таймвеб.Домены).')
    min_length = Column(TINYINT(3), nullable=False, server_default=text("'3'"), comment='Минимальная длина доменного имени (без учета разделительных точек и имени зоны)')
    sort_order = Column(SMALLINT(6), nullable=False, server_default=text("'1000'"), comment='Порядок выдачи доменов')
    min_register_period = Column(Enum('P1Y', 'P2Y', 'P3Y', 'P4Y', 'P5Y', 'P6Y', 'P7Y', 'P8Y', 'P9Y', 'P10Y'), nullable=False, server_default=text("'P1Y'"), comment='ISO 8601 duration - минимальный период для регистрации доменов.')
    max_register_period = Column(Enum('P1Y', 'P2Y', 'P3Y', 'P4Y', 'P5Y', 'P6Y', 'P7Y', 'P8Y', 'P9Y', 'P10Y'), nullable=False, server_default=text("'P1Y'"), comment='ISO 8601 duration - максимальный период для регистрации доменов.')
    min_prolong_period = Column(Enum('P1Y', 'P2Y', 'P3Y', 'P4Y', 'P5Y', 'P6Y', 'P7Y', 'P8Y', 'P9Y', 'P10Y'), nullable=False, server_default=text("'P1Y'"), comment='ISO 8601 duration - минимальный период для продления доменов.')
    max_prolong_period = Column(Enum('P1Y', 'P2Y', 'P3Y', 'P4Y', 'P5Y', 'P6Y', 'P7Y', 'P8Y', 'P9Y', 'P10Y'), nullable=False, server_default=text("'P1Y'"), comment='ISO 8601 duration - максимальный период для продления доменов.')
    use_blank_person = Column(TINYINT(1), nullable=False, server_default=text("'0'"), comment='Признак возможности использования незаполненной персоны в данной зоне')
    ssl_provider = Column(Enum('sslstore', 'global_sign'), nullable=False, server_default=text("'sslstore'"))
    disabled_by_registrar = Column(TINYINT(1), server_default=text("'0'"), comment='Блокированные регистратором зоны, для которых не отдаётся премиальная иформация')

    domain_providers = relationship('DomainProviders')
